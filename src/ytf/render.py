from __future__ import annotations
import csv
import json
import shutil
import subprocess
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from . import paths
from .jobs import Checkpoint, inputs_hash, with_retry, write_json
from .models import FORMATS, FPS, Episode
from .tts import Timeline

BRAND = {"name": "Plotted Past"}


def load_csv(p: Path) -> list[dict]:
    rows = []
    with open(p, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            row = {}
            for k, v in r.items():
                if v is None:
                    continue
                try:
                    row[k] = float(v) if ("." in v or "e" in v.lower()) else int(v)
                except ValueError:
                    row[k] = v
            rows.append(row)
    return rows


def build_payload(ep: Episode, scenes, tl: Timeline, fmt: str) -> dict:
    w, h = FORMATS[fmt]
    data = {k: load_csv(paths.episode_dir(ep.id) / v) for k, v in ep.data_files.items()}
    dur = {s.id: s.duration for s in tl.scenes}
    return {
        "id": ep.id, "title": ep.title, "format": {"w": w, "h": h, "name": fmt}, "brand": BRAND, "data": data,
        "scenes": [
            {"id": s.id, "kind": s.kind, "params": s.params, "caption": s.caption, "source": s.source, "duration": dur[s.id]}
            for s in scenes
        ],
    }


def write_page(payload: dict, out_dir: Path) -> Path:
    html = (paths.TEMPLATES / "base.html").read_text(encoding="utf-8")
    font = (paths.ASSETS / "fonts" / "Inter-Variable.ttf").resolve().as_uri()
    shutil.copy(paths.TEMPLATES / "scenes.js", out_dir / "scenes.js")
    html = (html.replace("__FONT_URL__", font).replace("__W__", str(payload["format"]["w"]))
            .replace("__H__", str(payload["format"]["h"])).replace("__PAYLOAD__", json.dumps(payload))
            .replace("__SCENES_JS__", "scenes.js"))
    p = out_dir / "page.html"
    p.write_text(html, encoding="utf-8")
    return p


def _open_page(pw, page_path: Path, w: int, h: int):
    browser = pw.chromium.launch(args=["--disable-gpu", "--font-render-hinting=none", "--disable-lcd-text"])
    page = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
    page.goto(page_path.resolve().as_uri(), wait_until="load")
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(150)
    return browser, page


def render_scene_task(args) -> dict:
    """Render one scene to a segment MP4 (runs in a worker process)."""
    page_path, idx, scene_id, duration, w, h, seg_path, frames_root, keep_frames, log = (
        Path(args["page"]), args["idx"], args["id"], args["duration"], args["w"], args["h"], Path(args["seg"]),
        Path(args["frames_root"]), args["keep_frames"], Path(args["log"]))
    from playwright.sync_api import sync_playwright
    n = int(round(duration * FPS))
    frames = frames_root / scene_id
    if frames.exists():
        shutil.rmtree(frames)
    frames.mkdir(parents=True)
    t0 = time.time()
    overflow = []
    with sync_playwright() as pw:
        browser, page = _open_page(pw, page_path, w, h)
        for i in range(n):
            t = i / FPS
            page.evaluate("([i,t])=>window.renderFrame(i,t)", [idx, t])
            if i == n // 2:
                overflow = page.evaluate("window.checkOverflow()")
            page.screenshot(path=str(frames / f"f{i:05d}.png"), type="png")
        browser.close()
    t_cap = time.time() - t0
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-framerate", str(FPS), "-i", str(frames / "f%05d.png"),
           "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-g", "60", "-r", str(FPS),
           "-vf", f"scale={w}:{h}", str(seg_path)]
    with_retry(lambda: subprocess.run(cmd, check=True), attempts=2, log=log, label=f"encode {scene_id}")
    if not keep_frames:
        shutil.rmtree(frames, ignore_errors=True)
    return {"id": scene_id, "frames": n, "capture_s": round(t_cap, 2), "encode_s": round(time.time() - t0 - t_cap, 2),
            "fps_capture": round(n / t_cap, 1) if t_cap else None, "overflow": overflow}


def render_video(ep: Episode, scenes, tl: Timeline, fmt: str, out_dir: Path, workers: int = 2, keep_frames: bool = False,
                 force: bool = False) -> Path:
    w, h = FORMATS[fmt]
    payload = build_payload(ep, scenes, tl, fmt)
    page = write_page(payload, out_dir)
    seg_dir = out_dir / "segments"; seg_dir.mkdir(exist_ok=True)
    frames_root = out_dir / "frames"
    log = out_dir / "error.log"
    ck = Checkpoint(out_dir / "ck")
    code_hash = inputs_hash([paths.TEMPLATES / "scenes.js", paths.TEMPLATES / "base.html"])
    tasks, stats = [], []
    for idx, s in enumerate(payload["scenes"]):
        h_in = inputs_hash([], extra=json.dumps([s, code_hash, w, h]))
        seg = seg_dir / f"{idx:02d}_{s['id']}.mp4"
        if not force and seg.exists() and ck.is_done(f"seg_{s['id']}", h_in):
            stats.append({"id": s["id"], "cached": True})
            continue
        tasks.append(({"page": str(page), "idx": idx, "id": s["id"], "duration": s["duration"], "w": w, "h": h, "seg": str(seg),
                       "frames_root": str(frames_root), "keep_frames": keep_frames, "log": str(log)}, h_in, s["id"]))
    if tasks:
        with ProcessPoolExecutor(max_workers=max(1, workers)) as ex:
            for (task, h_in, sid), res in zip(tasks, ex.map(render_scene_task, [t[0] for t in tasks])):
                ck.mark(f"seg_{sid}", h_in)
                stats.append(res)
    # concat
    lst = out_dir / "segments.txt"
    lines = []
    for i, s in enumerate(payload["scenes"]):
        seg_path = (seg_dir / f"{i:02d}_{s['id']}.mp4").resolve()
        lines.append(f"file '{seg_path}'\n")
    lst.write_text("".join(lines))
    video = out_dir / "video.mp4"
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy",
                    str(video)], check=True)
    write_json(out_dir / "render_stats.json", {"scenes": stats, "fps": FPS, "w": w, "h": h})
    return video


def render_thumbnail(ep: Episode, scenes, tl: Timeline, fmt: str, out_dir: Path) -> list[Path]:
    """Render thumbnail variants (1920x1080 capture → 1280x720 PNG) from a chosen scene/time + headline overlay."""
    from PIL import Image
    from playwright.sync_api import sync_playwright
    w, h = FORMATS["long"]
    payload = build_payload(ep, scenes, tl, "long")
    tdir = out_dir / "thumb"; tdir.mkdir(exist_ok=True)
    page_path = write_page(payload, tdir)
    outs = []
    ids = [s["id"] for s in payload["scenes"]]
    with sync_playwright() as pw:
        browser, page = _open_page(pw, page_path, w, h)
        for vi, var in enumerate(ep.thumbnail.variants or [{"headline": ep.title, "sub": "", "scene": ids[min(1, len(ids) - 1)], "t": 4.0}]):
            idx = ids.index(var.get("scene", ids[0]))
            page.evaluate("([i,t,s])=>window.renderFrame(i,t,s)", [idx, float(var.get("t", 4.0)), {"headline": var.get("headline", ""), "sub": var.get("sub", "")}])
            raw = tdir / f"thumb_{vi}_raw.png"
            page.screenshot(path=str(raw), type="png")
            im = Image.open(raw).convert("RGB").resize((1280, 720), Image.LANCZOS)
            p = tdir / f"thumbnail_{chr(65 + vi)}.png"; im.save(p, optimize=True)
            im.resize((320, 180), Image.LANCZOS).save(tdir / f"thumbnail_{chr(65 + vi)}_mobile320.png")
            outs.append(p)
        browser.close()
    return outs
