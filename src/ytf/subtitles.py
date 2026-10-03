from __future__ import annotations
from pathlib import Path
from .text import wrap_lines
from .tts import Timeline


def _ts(t: float, vtt: bool = False) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    sep = "." if vtt else ","
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def cues_from_timeline(tl: Timeline, max_chars: int = 42, max_lines: int = 2) -> list[tuple[float, float, str]]:
    cues = []
    for sc in tl.scenes:
        for s in sc.sentences:
            blocks = wrap_lines(s.text, max_chars, max_lines)
            total_chars = sum(len(" ".join(b)) for b in blocks) or 1
            t = s.start
            for b in blocks:
                frac = len(" ".join(b)) / total_chars
                dur = max(0.8, s.duration * frac)
                cues.append((t, min(t + dur, s.end if b is blocks[-1] else t + dur), "\n".join(b)))
                t += dur
    # fix overlaps
    out = []
    for i, (a, b, txt) in enumerate(cues):
        if i + 1 < len(cues):
            b = min(b, cues[i + 1][0] - 0.02)
        out.append((a, max(b, a + 0.5), txt))
    return out


def write_srt(tl: Timeline, path: Path) -> int:
    cues = cues_from_timeline(tl)
    lines = []
    for i, (a, b, txt) in enumerate(cues, 1):
        lines += [str(i), f"{_ts(a)} --> {_ts(b)}", txt, ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    return len(cues)


def write_vtt(tl: Timeline, path: Path) -> int:
    cues = cues_from_timeline(tl)
    lines = ["WEBVTT", ""]
    for a, b, txt in cues:
        lines += [f"{_ts(a, True)} --> {_ts(b, True)}", txt, ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    return len(cues)
