from __future__ import annotations
import json
import re
import subprocess
from pathlib import Path


def measure_loudness(audio: Path) -> dict:
    cmd = ["ffmpeg", "-hide_banner", "-nostats", "-i", str(audio), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    m = re.search(r"\{.*\}", r.stderr, re.S)
    if not m:
        raise RuntimeError("loudnorm measurement failed: " + r.stderr[-800:])
    return json.loads(m.group(0))


def mux(video: Path, narration: Path, out: Path) -> dict:
    """Two-pass loudnorm (-14 LUFS, -1.5 dBTP), AAC 192k 48 kHz, pad audio to video length."""
    m = measure_loudness(narration)
    ln = ("loudnorm=I=-14:TP=-1.5:LRA=11:linear=true:measured_I={input_i}:measured_TP={input_tp}:measured_LRA={input_lra}:"
          "measured_thresh={input_thresh}:offset={target_offset}").format(**m)
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(video), "-i", str(narration),
           "-af", f"{ln},alimiter=limit=0.8:attack=3:release=60:level=false,aresample=48000,apad", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
           "-shortest", "-movflags", "+faststart", str(out)]
    subprocess.run(cmd, check=True)
    # verify; loudnorm linear mode can land >0.5 LU off target — correct with a plain gain and re-mux (max 2 passes)
    for _ in range(2):
        got = measure_loudness(out)
        diff = -14.0 - float(got["input_i"])
        if abs(diff) <= 0.4 and float(got["input_tp"]) <= -1.0:
            break
        tmp = out.with_name(out.stem + "_gain.mp4")
        # gain, then a true-peak-safe limiter at -1.9 dBTP (speech has a high peak-to-loudness ratio)
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(out), "-af", f"volume={diff:.2f}dB,alimiter=limit=0.8:attack=3:release=60:level=false",
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(tmp)], check=True)
        tmp.replace(out)
    return m


def ffprobe(path: Path) -> dict:
    r = subprocess.run(["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", str(path)],
                       capture_output=True, text=True, check=True)
    return json.loads(r.stdout)
