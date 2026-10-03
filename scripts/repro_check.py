#!/usr/bin/env python3
"""Reproducibility check between two builds of the same episode (MASTER_PLAN §6 tolerances).
Usage: uv run python scripts/repro_check.py build/ep-001/long /path/to/other/build/ep-001/long [--frames 6]
Compares: duration, frame count, SRT cue count, per-sentence durations (±20 ms), loudness (±0.5 LU), sampled frame pixel diff (<1/255 mean),
and reports whether MP4 sha256 happen to be identical (not required)."""
import hashlib, json, subprocess, sys, tempfile
from pathlib import Path
import numpy as np
from PIL import Image

a, b = Path(sys.argv[1]), Path(sys.argv[2])
nf = int(sys.argv[sys.argv.index("--frames") + 1]) if "--frames" in sys.argv else 6
ep = next(a.glob("ep-*.mp4")).name
A, B = a / ep, b / ep

def probe(p):
    j = json.loads(subprocess.run(["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", str(p)], capture_output=True, text=True).stdout)
    v = next(s for s in j["streams"] if s["codec_type"] == "video")
    return float(j["format"]["duration"]), int(v.get("nb_frames", 0))

def loud(p):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-af", "loudnorm=print_format=json", "-f", "null", "-"], capture_output=True, text=True)
    import re; return float(json.loads(re.search(r"\{.*\}", r.stderr, re.S).group(0))["input_i"])

def sha(p):
    h = hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()

def frame(p, t, out):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{t:.3f}", "-i", str(p), "-frames:v", "1", str(out)], check=True)
    return np.asarray(Image.open(out).convert("RGB"), dtype=np.float32)

res = {}
(da, fa), (db, fb) = probe(A), probe(B)
res["duration"] = {"a": da, "b": db, "ok": abs(da - db) <= 1 / 30 + 1e-3}
res["frames"] = {"a": fa, "b": fb, "ok": fa == fb}
ta, tb = json.loads((a / "timeline.json").read_text()), json.loads((b / "timeline.json").read_text())
sa = [s["duration"] for sc in ta["scenes"] for s in sc["sentences"]]; sb = [s["duration"] for sc in tb["scenes"] for s in sc["sentences"]]
res["sentences"] = {"n_a": len(sa), "n_b": len(sb), "max_abs_diff_ms": round(1000 * max((abs(x - y) for x, y in zip(sa, sb)), default=0), 1),
                    "ok": len(sa) == len(sb) and all(abs(x - y) <= 0.02 for x, y in zip(sa, sb))}
ca, cb = (a / f"{ep[:-4]}.srt").read_text().count("-->"), (b / f"{ep[:-4]}.srt").read_text().count("-->")
res["srt_cues"] = {"a": ca, "b": cb, "ok": ca == cb}
la, lb = loud(A), loud(B)
res["loudness"] = {"a": la, "b": lb, "ok": abs(la - lb) <= 0.5}
with tempfile.TemporaryDirectory() as td:
    diffs = []
    for i in range(nf):
        t = da * (i + 0.5) / nf
        x, y = frame(A, t, Path(td) / "a.png"), frame(B, t, Path(td) / "b.png")
        diffs.append(float(np.abs(x - y).mean()) / 255)
res["frames_pixel_diff"] = {"mean_per_sample": [round(d, 5) for d in diffs], "ok": max(diffs) < 1 / 255}
ha, hb = sha(A), sha(B)
res["mp4_sha256_identical"] = ha == hb
res["REPRODUCIBLE"] = all(v["ok"] for k, v in res.items() if isinstance(v, dict))
print(json.dumps(res, indent=2))
