from __future__ import annotations
import re

_ABBREV = ("Dr", "Mr", "Mrs", "Ms", "St", "No", "vs", "Fig", "Lt", "Gen", "Col", "Prof", "Sgt", "Capt", "Jr", "Sr", "U.S", "e.g", "i.e")
_SPLIT = re.compile(r"(?<=[.!?])[\"')\]]?\s+(?=[A-Z0-9\"'(\[])")


def split_sentences(text: str) -> list[str]:
    text = " ".join(text.split())
    if not text:
        return []
    # protect abbreviations
    prot = text
    for a in _ABBREV:
        prot = re.sub(rf"\b{re.escape(a)}\.", a.replace(".", "<DOT>") + "<DOT>", prot)
    parts = _SPLIT.split(prot)
    out = []
    for p in parts:
        p = p.replace("<DOT>", ".").strip()
        if p:
            out.append(p)
    return out


def wrap_lines(text: str, max_chars: int = 42, max_lines: int = 2) -> list[list[str]]:
    """Split a sentence into cue blocks of <=max_lines lines, each <=max_chars."""
    words = text.split()
    lines: list[str] = []
    cur = ""
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) <= max_chars:
            cur = f"{cur} {w}".strip()
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    blocks = [lines[i:i + max_lines] for i in range(0, len(lines), max_lines)]
    return blocks or [[text]]


def normalize_for_wer(s: str) -> list[str]:
    s = s.lower()
    s = re.sub(r"[^a-z0-9' ]+", " ", s)
    return s.split()


def wer(ref: str, hyp: str) -> float:
    r, h = normalize_for_wer(ref), normalize_for_wer(hyp)
    if not r:
        return 0.0 if not h else 1.0
    d = [[0] * (len(h) + 1) for _ in range(len(r) + 1)]
    for i in range(len(r) + 1):
        d[i][0] = i
    for j in range(len(h) + 1):
        d[0][j] = j
    for i in range(1, len(r) + 1):
        for j in range(1, len(h) + 1):
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (r[i - 1] != h[j - 1]))
    return d[-1][-1] / len(r)
