from __future__ import annotations
import json
import re
import subprocess
import time
from pathlib import Path
import numpy as np
import soundfile as sf

from . import paths
from .assemble import ffprobe, measure_loudness
from .jobs import write_json
from .models import FORMATS, FPS, Episode
from .text import split_sentences, wer
from .tts import Timeline, phonemes_for

_asr = None


def get_asr():
    global _asr
    if _asr is None:
        import sherpa_onnx
        d = paths.WHISPER_DIR
        if not d.exists():
            raise FileNotFoundError("Whisper model missing; run scripts/fetch_models.py")
        _asr = sherpa_onnx.OfflineRecognizer.from_whisper(
            encoder=str(d / "base.en-encoder.int8.onnx"), decoder=str(d / "base.en-decoder.int8.onnx"),
            tokens=str(d / "base.en-tokens.txt"), num_threads=4, language="en", task="transcribe")
    return _asr


def transcribe(wav: Path) -> str:
    a, sr = sf.read(wav, dtype="float32")
    if a.ndim > 1:
        a = a.mean(axis=1)
    rec = get_asr()
    s = rec.create_stream(); s.accept_waveform(sr, a); rec.decode_stream(s)
    return s.result.text.strip()


def ffmpeg_detect(path: Path, flt: str) -> list[str]:
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-vf" if "black" in flt else "-af", flt, "-f", "null", "-"],
                       capture_output=True, text=True)
    return [l.strip() for l in r.stderr.splitlines() if "detect" in l and ("start" in l or "duration" in l)]


def spectrogram_png(wav: Path, out: Path, width: int = 1800, height: int = 360, px_per_s: float | None = None) -> None:
    """Log-power spectrogram, 0–5 kHz, dB range -75..-5 relative to full scale; px_per_s overrides width for zoomed views."""
    from PIL import Image
    a, sr = sf.read(wav, dtype="float32")
    if a.ndim > 1:
        a = a.mean(axis=1)
    if px_per_s:
        width = max(200, int(len(a) / sr * px_per_s))
    n = 1024
    hop = max(64, len(a) // width)
    win = np.hanning(n)
    fmax_bin = int(5000 / (sr / n))
    cols = []
    for i in range(0, max(1, len(a) - n), hop):
        seg = a[i:i + n]
        if len(seg) < n:
            seg = np.pad(seg, (0, n - len(seg)))
        mag = np.abs(np.fft.rfft(seg * win))[:fmax_bin] / (n / 4)
        cols.append(20 * np.log10(mag + 1e-7))
    S = np.array(cols).T
    S = np.clip((S + 75) / 70, 0, 1) ** 0.8
    img = (255 * S[::-1]).astype(np.uint8)
    Image.fromarray(img).resize((width, height), Image.BILINEAR).save(out)
    # waveform
    wv = np.zeros((160, width), dtype=np.uint8)
    step = max(1, len(a) // width)
    for x in range(width):
        seg = a[x * step:(x + 1) * step]
        if len(seg):
            lo, hi = int(80 - 78 * max(-1, seg.min())), int(80 - 78 * min(1, seg.max()))
            wv[min(lo, hi):max(lo, hi) + 1, x] = 255
    Image.fromarray(wv).save(out.with_name(out.stem + "_wave.png"))


def content_fraction(img: Path, bg=(11, 16, 32), thr: int = 24) -> float:
    """Fraction of pixels that differ from the brand background — catches blank/frozen scenes that blackdetect cannot."""
    from PIL import Image
    a = np.asarray(Image.open(img).convert("RGB"), dtype=np.int16)
    return float((np.abs(a - np.array(bg, dtype=np.int16)).max(axis=2) > thr).mean())


def sample_frames(video: Path, tl: Timeline, out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    outs = []
    for sc in tl.scenes:
        for tag, t in (("a", sc.start + min(1.2, sc.duration * .3)), ("b", sc.start + sc.duration * .75)):
            p = out_dir / f"{sc.id}_{tag}.jpg"
            subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{t:.3f}", "-i", str(video), "-frames:v", "1",
                            "-q:v", "3", str(p)], check=True)
            outs.append(p)
    return outs


def run_qc(ep: Episode, fmt: str, bdir: Path, final: Path, tl: Timeline, report_dir: Path, do_asr: bool = True) -> dict:
    report_dir.mkdir(parents=True, exist_ok=True)
    w, h = FORMATS[fmt]
    res: dict = {"episode": ep.id, "format": fmt, "checks": {}, "audio_eval": {}, "warnings": [], "status": "QC_FAIL"}
    ck = res["checks"]
    info = ffprobe(final)
    v = next(s for s in info["streams"] if s["codec_type"] == "video")
    a = next(s for s in info["streams"] if s["codec_type"] == "audio")
    dur = float(info["format"]["duration"])
    nb_frames = int(v.get("nb_frames") or round(dur * FPS))
    expected_frames = sum(int(round(s.duration * FPS)) for s in tl.scenes)
    ck["container"] = {"codec": v["codec_name"], "pix_fmt": v.get("pix_fmt"), "w": v["width"], "h": v["height"], "fps": v["r_frame_rate"],
                       "audio": f"{a['codec_name']} {a.get('sample_rate')}Hz", "duration": round(dur, 3), "frames": nb_frames,
                       "expected_frames": expected_frames,
                       "ok": v["codec_name"] == "h264" and v.get("pix_fmt") == "yuv420p" and v["width"] == w and v["height"] == h
                       and v["r_frame_rate"] == f"{FPS}/1" and a["codec_name"] == "aac" and abs(nb_frames - expected_frames) <= 1}
    black = ffmpeg_detect(final, "blackdetect=d=1.0:pix_th=0.05")  # brand background (#0B1020, luma≈0.064) is NOT black; true black only
    sil = ffmpeg_detect(final, "silencedetect=noise=-50dB:d=2.5")
    ck["blackdetect"] = {"events": black, "ok": len(black) == 0}
    # silences longer than 2.5 s are expected only at scene boundaries (pad) — report count, pass if <= scenes
    ck["silencedetect"] = {"events": sil, "ok": len([l for l in sil if "silence_start" in l]) <= len(tl.scenes) + 1}
    ln = measure_loudness(final)
    ck["loudness"] = {"integrated_lufs": float(ln["input_i"]), "true_peak_dbtp": float(ln["input_tp"]), "lra": float(ln["input_lra"]),
                      "ok": abs(float(ln["input_i"]) + 14) <= 1.0 and float(ln["input_tp"]) <= -1.0}
    # subtitles
    srt = bdir / f"{ep.id}.srt"
    cues = re.findall(r"(\d+:\d\d:\d\d,\d{3}) --> (\d+:\d\d:\d\d,\d{3})\n(.+?)(?:\n\n|\Z)", srt.read_text(encoding="utf-8"), re.S)
    long_lines = [c for c in cues if any(len(l) > 42 for l in c[2].strip().split("\n")) or len(c[2].strip().split("\n")) > 2]
    ck["subtitles"] = {"cues": len(cues), "long_or_tall": len(long_lines), "ok": len(cues) > 0 and not long_lines}
    rs = json.loads((bdir / "render_stats.json").read_text())
    overflow = [s for s in rs["scenes"] if s.get("overflow")]
    ck["text_overflow"] = {"scenes": [{"id": s["id"], "items": s["overflow"]} for s in overflow], "ok": not overflow}
    frames = sample_frames(final, tl, report_dir / "frames")
    ck["frame_samples"] = {"count": len(frames), "dir": str(report_dir / "frames"), "reviewed_by_claude": ep.gate.frames_reviewed}
    blank = []
    for fp in frames:
        frac = content_fraction(fp)
        if frac < 0.002:
            blank.append({"frame": fp.name, "content_fraction": round(frac, 5)})
    ck["frame_content"] = {"blank_frames": blank, "ok": not blank}
    # ---- audio evaluation layers ----
    sents = [(sc.id, s) for sc in tl.scenes for s in sc.sentences]
    spectrogram_png(bdir / "narration_raw.wav", report_dir / "spectrogram.png")
    res["audio_eval"]["spectrogram"] = str(report_dir / "spectrogram.png")
    texts = [s.text for _, s in sents]
    res["audio_eval"]["phonemes"] = [{"scene": sid, "text": s.text, "ipa": ipa} for (sid, s), ipa in zip(sents, phonemes_for(texts, ep.language))]
    if do_asr:
        rows = []
        t0 = time.time()
        for sid, s in sents:
            hyp = transcribe(Path(s.wav))
            rows.append({"scene": sid, "ref": s.text, "hyp": hyp, "wer": round(wer(s.text, hyp), 3)})
        flagged = [r for r in rows if r["wer"] > 0.05]
        zoom_dir = report_dir / "spectrograms"; zoom_dir.mkdir(exist_ok=True)
        for k, f in enumerate(flagged[:8]):
            wavp = next((s.wav for sid, s in sents if s.text == f["ref"]), None)
            if wavp:
                spectrogram_png(Path(wavp), zoom_dir / f"flag_{k:02d}_{f['scene']}.png", height=300, px_per_s=150)
                f["spectrogram"] = str(zoom_dir / f"flag_{k:02d}_{f['scene']}.png")
        res["audio_eval"]["asr"] = {"model": "whisper-base.en int8 (sherpa-onnx)", "seconds": round(time.time() - t0, 1), "rows": rows,
                                    "mean_wer": round(sum(r["wer"] for r in rows) / max(1, len(rows)), 4), "flagged": flagged}
    res["audio_eval"]["disclaimer"] = ("Audio was evaluated by phoneme review, ASR round-trip and spectrogram inspection; "
                                       "no human listening test was performed.")
    tech_ok = all(c.get("ok", True) for c in ck.values() if isinstance(c, dict) and "ok" in c)
    res["technical_ok"] = tech_ok
    res["gate"] = ep.gate.model_dump()
    res["gate_ok"] = ep.gate.all_ok()
    audio_layers_ok = do_asr and bool(res["audio_eval"].get("phonemes"))
    audio_reviewed = ep.gate.audio_reviewed and ep.gate.frames_reviewed
    if tech_ok and res["gate_ok"] and audio_layers_ok and audio_reviewed:
        res["status"] = "QC_PASS"  # flagged ASR rows must have been reviewed and explained in gate.notes
    elif tech_ok:
        res["status"] = "QC_PASS_TECHNICAL_ONLY"
    write_json(report_dir / "qc.json", res)
    (report_dir / "qc-report.md").write_text(render_report(res), encoding="utf-8")
    return res


def render_report(r: dict) -> str:
    L = [f"# QC report — {r['episode']} ({r['format']})", "", f"**Status:** `{r['status']}`  •  technical_ok={r['technical_ok']}  •  gate_ok={r['gate_ok']}", ""]
    L += ["## B. Technical checks", "| check | ok | detail |", "|---|---|---|"]
    for k, c in r["checks"].items():
        detail = {kk: vv for kk, vv in c.items() if kk not in ("ok", "events", "scenes", "items")}
        extra = ""
        if c.get("events"): extra = f" events={len(c['events'])}"
        if c.get("scenes"): extra = f" overflow_scenes={[s['id'] for s in c['scenes']]}"
        L.append(f"| {k} | {'✅' if c.get('ok', True) else '❌'} | {json.dumps(detail, ensure_ascii=False)[:300]}{extra} |")
    L += ["", "## C. Audio evaluation (not a human listening test)", f"> {r['audio_eval'].get('disclaimer','')}", ""]
    asr = r["audio_eval"].get("asr")
    if asr:
        L += [f"ASR: {asr['model']} — mean WER **{asr['mean_wer']}**, flagged (WER>0.05): {len(asr['flagged'])}", ""]
        for f in asr["flagged"]:
            L += [f"- [{f['scene']}] WER {f['wer']}: ref=`{f['ref']}` hyp=`{f['hyp']}`"]
        L += [""]
    L += ["<details><summary>Phoneme review (IPA per sentence)</summary>", ""]
    for p in r["audio_eval"].get("phonemes", []):
        L += [f"- [{p['scene']}] {p['text']}", f"  - `{p['ipa']}`"]
    L += ["", "</details>", "", f"Spectrogram: `{r['audio_eval'].get('spectrogram')}` (+ `_wave.png`)", ""]
    L += ["## A. Content gate (manual)", "| item | ok |", "|---|---|"]
    for k, v in r["gate"].items():
        if k != "notes":
            L.append(f"| {k} | {'✅' if v else '❌'} |")
    if r["gate"].get("notes"):
        L += ["", f"Notes: {r['gate']['notes']}"]
    L += ["", f"Frame samples: `{r['checks']['frame_samples']['dir']}` — reviewed_by_claude={r['checks']['frame_samples']['reviewed_by_claude']}"]
    return "\n".join(L) + "\n"
