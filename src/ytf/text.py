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


_ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
         "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
_TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def num_to_words(n: int) -> str:
    """Plain English, matching how narration is written (e.g. 1,023 -> one thousand twenty three; years 1855 -> eighteen fifty five)."""
    if n < 20:
        return _ONES[n]
    if n < 100:
        return _TENS[n // 10] + ("" if n % 10 == 0 else " " + _ONES[n % 10])
    if n < 1000:
        return _ONES[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + num_to_words(n % 100))
    if 1100 <= n <= 1999 and n % 100 != 0:  # year-style
        return num_to_words(n // 100) + " " + num_to_words(n % 100)
    if n < 1_000_000:
        return num_to_words(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + num_to_words(n % 1000))
    return num_to_words(n // 1_000_000) + " million" + ("" if n % 1_000_000 == 0 else " " + num_to_words(n % 1_000_000))


_ORD = {"one": "first", "two": "second", "three": "third", "five": "fifth", "eight": "eighth", "nine": "ninth", "twelve": "twelfth"}


def ordinal_words(n: int) -> str:
    w = num_to_words_plain(n).split()
    last = w[-1]
    if last in _ORD:
        w[-1] = _ORD[last]
    elif last.endswith("y"):
        w[-1] = last[:-1] + "ieth"
    else:
        w[-1] = last + "th"
    return " ".join(w)


def num_to_words_plain(n: int) -> str:
    """Same as num_to_words but never uses the year style (1758 -> one thousand seven hundred fifty eight)."""
    if 1100 <= n <= 1999 and n % 100 != 0:
        return num_to_words(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + num_to_words(n % 1000))
    return num_to_words(n)


# ASR/TTS-neutral spellings: both sides are mapped before comparison (homophones and spacing variants only).
_HOMOPHONES = {"cockscomb": "coxcomb", "far": "farr", "scatter plot": "scatterplot", "scatterplots": "scatterplot",
               "o rings": "orings", "o ring": "oring", "orings": "oring", "percent": "per cent", "ok": "okay",
               "colour": "color", "colours": "colors", "grey": "gray", "metre": "meter", "metres": "meters", "centre": "center"}


def normalize_for_wer(s: str, year_style: bool = True) -> list[str]:
    s = s.lower()
    s = re.sub(r"\[[^\]]*\]", " ", s)          # whisper tags like [AUDIO OUT]
    s = s.replace("°f", " degrees fahrenheit ").replace("°", " degrees ")
    s = re.sub(r"(\d),(\d{3})", r"\1\2", s)       # 1,023 -> 1023
    s = re.sub(r"\b([2-9])0s\b", lambda m: _TENS[int(m.group(1))][:-1] + "ies", s)  # 50s -> fifties
    s = re.sub(r"\b(\d+)(st|nd|rd|th)\b", lambda m: " " + ordinal_words(int(m.group(1))) + " ", s)  # 31st -> thirty first
    s = s.replace("'", "")                          # Snow's == Snows (ASR often drops possessives)
    s = re.sub(r"\d+", lambda m: " " + (num_to_words(int(m.group(0))) if year_style else num_to_words_plain(int(m.group(0)))) + " ", s)
    s = re.sub(r"[^a-z ]+", " ", s)
    s = re.sub(r"\b(and)\b", " ", s)             # "four hundred and seventy six" == "four hundred seventy six"
    s = re.sub(r"-", " ", s)
    s = " ".join(s.split())
    for a, b in _HOMOPHONES.items():
        s = re.sub(rf"\b{a}\b", b, s)
    return s.split()


def wer(ref: str, hyp: str) -> float:
    """Word error rate after normalization; digits in the hypothesis may be read as years or plain numbers — take the better."""
    return min(_wer(normalize_for_wer(ref), normalize_for_wer(hyp, True)), _wer(normalize_for_wer(ref), normalize_for_wer(hyp, False)))


def _wer(r: list[str], h: list[str]) -> float:
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
