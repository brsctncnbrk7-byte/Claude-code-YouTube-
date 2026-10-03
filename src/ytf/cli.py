from __future__ import annotations
import argparse
import json
import sys
import time
from pathlib import Path
import yaml

from . import paths
from .jobs import Checkpoint, inputs_hash, write_json
from .models import Episode
from .tts import Timeline


def _load(ep_id: str) -> Episode:
    p = paths.episode_dir(ep_id) / "episode.yaml"
    if not p.exists():
        sys.exit(f"missing {p}")
    return Episode.load(p)


def _timeline(bdir: Path) -> Timeline:
    return Timeline.from_json(json.loads((bdir / "timeline.json").read_text()))


def cmd_build(a):
    from .render import render_video
    from .subtitles import write_srt, write_vtt
    from .tts import build_narration
    from .assemble import mux
    ep = _load(a.episode)
    fmt = a.format
    scenes = ep.scenes_for(fmt)
    bdir = paths.build_dir(ep.id, fmt)
    ck = Checkpoint(bdir / "ck")
    if a.force:
        ck.clear()
    t0 = time.time()
    h_tts = inputs_hash([paths.episode_dir(ep.id) / "episode.yaml"], extra=f"tts|{fmt}|{ep.voice}|{ep.speed}")
    if ck.is_done("tts", h_tts) and (bdir / "timeline.json").exists():
        tl = _timeline(bdir); print(f"[tts] cached ({tl.total:.1f}s)")
    else:
        tl = build_narration(scenes, ep.voice, ep.speed, ep.language, bdir)
        ck.mark("tts", h_tts); print(f"[tts] {tl.total:.1f}s narration, {sum(len(s.sentences) for s in tl.scenes)} sentences, {time.time()-t0:.1f}s")
    n = write_srt(tl, bdir / f"{ep.id}.srt"); write_vtt(tl, bdir / f"{ep.id}.vtt"); print(f"[subs] {n} cues")
    t1 = time.time()
    video = render_video(ep, scenes, tl, fmt, bdir, workers=a.workers, keep_frames=a.keep_frames, force=a.force)
    print(f"[render] {video} in {time.time()-t1:.1f}s")
    final = bdir / f"{ep.id}.mp4"
    m = mux(video, bdir / "narration_raw.wav", final)
    print(f"[mux] {final} (measured I={m['input_i']} LUFS → -14)")
    write_json(bdir / "build_stats.json", {"total_seconds": round(time.time() - t0, 1), "narration_seconds": tl.total})
    print(f"[done] build {ep.id}/{fmt} in {time.time()-t0:.1f}s")


def cmd_qc(a):
    from .qc import run_qc
    ep = _load(a.episode); fmt = a.format
    bdir = paths.build_dir(ep.id, fmt)
    final = bdir / f"{ep.id}.mp4"
    if not final.exists():
        sys.exit("build first")
    res = run_qc(ep, fmt, bdir, final, _timeline(bdir), paths.REPORTS / ep.id / fmt, do_asr=not a.no_asr)
    print(f"[qc] {res['status']} technical_ok={res['technical_ok']} gate_ok={res['gate_ok']} → reports/{ep.id}/{fmt}/qc-report.md")


def cmd_package(a):
    from .package import make_package
    from .render import render_thumbnail
    ep = _load(a.episode); fmt = a.format
    bdir = paths.build_dir(ep.id, fmt)
    tl = _timeline(bdir)
    qc_path = paths.REPORTS / ep.id / fmt / "qc.json"
    qc = json.loads(qc_path.read_text()) if qc_path.exists() else {"status": "NOT_RUN"}
    thumbs = render_thumbnail(ep, ep.scenes, _timeline(paths.build_dir(ep.id, "long")), "long", bdir) if fmt == "long" else []
    d = make_package(ep, fmt, bdir, bdir / f"{ep.id}.mp4", tl, qc, thumbs)
    print(f"[package] {d}")


def cmd_status(a):
    q = yaml.safe_load((paths.CONTENT / "queue.yaml").read_text())
    for e in q["episodes"]:
        d = paths.DIST / e["id"]
        built = (paths.BUILD / e["id"] / "long" / f"{e['id']}.mp4").exists()
        print(f"{e['id']:7s} {e['status']:11s} built={'Y' if built else '-'} packaged={'Y' if (d / 'manifest.json').exists() else '-'}  {e['title_working']}")


def cmd_voices(a):
    from .tts import list_voices, synth_sentence
    text = a.text or "In 1858, Florence Nightingale drew a chart that no one in Parliament could ignore."
    out = paths.BUILD / "_voice_preview"; out.mkdir(parents=True, exist_ok=True)
    for v in (a.voices.split(",") if a.voices else list_voices()):
        s = synth_sentence(text, v, 1.0, "en-gb" if v.startswith("b") else "en-us", out)
        print(f"{v:12s} {s.duration:5.2f}s {s.wav}")


def cmd_all(a):
    cmd_build(a); cmd_qc(a); cmd_package(a)


def main(argv=None):
    p = argparse.ArgumentParser(prog="ytf", description="Plotted Past production pipeline")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name, fn in (("build", cmd_build), ("qc", cmd_qc), ("package", cmd_package), ("all", cmd_all)):
        s = sub.add_parser(name); s.add_argument("episode"); s.add_argument("--format", choices=["long", "short"], default="long")
        s.add_argument("--workers", type=int, default=2); s.add_argument("--keep-frames", action="store_true")
        s.add_argument("--force", action="store_true"); s.add_argument("--no-asr", action="store_true"); s.set_defaults(fn=fn)
    s = sub.add_parser("status"); s.set_defaults(fn=cmd_status)
    s = sub.add_parser("voices"); s.add_argument("--voices", default="af_heart,af_bella,am_michael,bm_george,bf_emma,am_adam,af_nova,bm_lewis"); s.add_argument("--text", default=None); s.set_defaults(fn=cmd_voices)
    a = p.parse_args(argv)
    a.fn(a)


if __name__ == "__main__":
    main()
