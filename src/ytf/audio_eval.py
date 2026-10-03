"""Deep audio evaluation on the *actual synthesized sentences* (free, offline, no user action):
1. Intelligibility: ASR round-trip with two Whisper models (base.en always; small.en when present) → per-sentence WER, best-of-two.
2. Perceptual quality: DNSMOS P.835 (Microsoft DNS-Challenge, CC BY 4.0) → SIG/BAK/OVRL MOS estimates per sentence.
3. Pronunciation of proper nouns/numbers: flagged sentences are listed with both transcripts and the G2P phonemes for review.
These are machine proxies; the report states explicitly that no human listening test was performed."""
from __future__ import annotations
import json
import subprocess
import tempfile
from pathlib import Path
import numpy as np
import soundfile as sf

from . import paths
from .text import wer
from .tts import Timeline, phonemes_for

DNSMOS_DIR = paths.MODELS / "dnsmos"
WHISPER_SMALL = paths.MODELS / "asr" / "sherpa-onnx-whisper-small.en"
# non-personalized polynomial mapping from dnsmos_local.py (lines 39-41 of the reference implementation)
_P_OVR = np.poly1d([-0.06766283, 1.11546468, 0.04602535])
_P_SIG = np.poly1d([-0.08397278, 1.22083953, 0.0052439])
_P_BAK = np.poly1d([-0.13166888, 1.60915514, -0.39604546])
_dnsmos = None
_asr_small = None


def _to16k(wav: Path) -> np.ndarray:
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as t:
        out = Path(t.name)
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(wav), "-ac", "1", "-ar", "16000", str(out)], check=True)
    a, _ = sf.read(out, dtype="float32")
    out.unlink(missing_ok=True)
    return a


def dnsmos(wav: Path) -> dict | None:
    """DNSMOS P.835 (sig_bak_ovr.onnx): 9.01 s windows at 16 kHz, 1 s hop, mean over windows (as in dnsmos_local.py)."""
    global _dnsmos
    model = DNSMOS_DIR / "sig_bak_ovr.onnx"
    if not model.exists():
        return None
    if _dnsmos is None:
        import onnxruntime as ort
        so = ort.SessionOptions(); so.intra_op_num_threads = 2
        _dnsmos = ort.InferenceSession(str(model), so, providers=["CPUExecutionProvider"])
    fs, L = 16000, 9.01
    a = _to16k(wav)
    n = int(L * fs)
    while len(a) < n:
        a = np.append(a, a)
    hops = int(np.floor(len(a) / fs) - L) + 1
    sig, bak, ovr = [], [], []
    for i in range(max(1, hops)):
        seg = a[int(i * fs): int((i + L) * fs)]
        if len(seg) < n:
            continue
        s, b, o = _dnsmos.run(None, {"input_1": seg.astype(np.float32)[np.newaxis, :]})[0][0]
        sig.append(float(_P_SIG(s))); bak.append(float(_P_BAK(b))); ovr.append(float(_P_OVR(o)))
    return {"sig": round(float(np.mean(sig)), 2), "bak": round(float(np.mean(bak)), 2), "ovrl": round(float(np.mean(ovr)), 2)}


def transcribe_small(wav: Path) -> str | None:
    global _asr_small
    if not (WHISPER_SMALL / "small.en-encoder.int8.onnx").exists():
        return None
    if _asr_small is None:
        import sherpa_onnx
        d = WHISPER_SMALL
        _asr_small = sherpa_onnx.OfflineRecognizer.from_whisper(
            encoder=str(d / "small.en-encoder.int8.onnx"), decoder=str(d / "small.en-decoder.int8.onnx"),
            tokens=str(d / "small.en-tokens.txt"), num_threads=4, language="en", task="transcribe")
    a, sr = sf.read(wav, dtype="float32")
    if a.ndim > 1:
        a = a.mean(axis=1)
    s = _asr_small.create_stream(); s.accept_waveform(sr, a); _asr_small.decode_stream(s)
    return s.result.text.strip()


# heuristic thresholds (documented in docs/policies/production-gate.md §C): DNSMOS was trained on real speech; clean TTS
# typically scores OVRL 3.0–3.6. WER thresholds: best-of-two-models.
THRESHOLDS = {"mean_wer_max": 0.05, "sentence_wer_max": 0.34, "ovrl_median_min": 3.0, "ovrl_sentence_min": 2.6}


def evaluate(ep_id: str, fmt: str, tl: Timeline, lang: str, out_dir: Path, base_rows: list[dict] | None = None) -> dict:
    """base_rows: per-sentence ASR rows from qc.py (base.en) to avoid re-transcribing."""
    out_dir.mkdir(parents=True, exist_ok=True)
    from .qc import transcribe  # base.en
    sents = [(sc.id, s) for sc in tl.scenes for s in sc.sentences]
    base_map = {(r["scene"], r["ref"]): r for r in (base_rows or [])}
    ipa = phonemes_for([s.text for _, s in sents], lang)
    rows = []
    for (sid, s), ph in zip(sents, ipa):
        hb = base_map.get((sid, s.text), {}).get("hyp") or transcribe(Path(s.wav))
        hs = transcribe_small(Path(s.wav))
        wb = round(wer(s.text, hb), 3); ws = round(wer(s.text, hs), 3) if hs is not None else None
        best = min(wb, ws) if ws is not None else wb
        q = dnsmos(Path(s.wav))
        rows.append({"scene": sid, "text": s.text, "duration": round(s.duration, 2), "ipa": ph, "hyp_base": hb, "wer_base": wb,
                     "hyp_small": hs, "wer_small": ws, "wer_best": best, "dnsmos": q})
    wers = [r["wer_best"] for r in rows]
    ovrls = [r["dnsmos"]["ovrl"] for r in rows if r["dnsmos"]]
    summary = {
        "sentences": len(rows), "mean_wer_best": round(float(np.mean(wers)), 4) if wers else None,
        "mean_wer_base": round(float(np.mean([r["wer_base"] for r in rows])), 4) if rows else None,
        "mean_wer_small": round(float(np.mean([r["wer_small"] for r in rows if r["wer_small"] is not None])), 4) if any(r["wer_small"] is not None for r in rows) else None,
        "models": ["whisper-base.en int8"] + (["whisper-small.en int8"] if any(r["wer_small"] is not None for r in rows) else []),
        "dnsmos_available": bool(ovrls),
        "ovrl_median": round(float(np.median(ovrls)), 2) if ovrls else None, "ovrl_min": round(float(np.min(ovrls)), 2) if ovrls else None,
        "sig_median": round(float(np.median([r["dnsmos"]["sig"] for r in rows if r["dnsmos"]])), 2) if ovrls else None,
        "bak_median": round(float(np.median([r["dnsmos"]["bak"] for r in rows if r["dnsmos"]])), 2) if ovrls else None,
    }
    flagged = [r for r in rows if r["wer_best"] > THRESHOLDS["sentence_wer_max"] or (r["dnsmos"] and r["dnsmos"]["ovrl"] < THRESHOLDS["ovrl_sentence_min"])]
    low_wer = [r for r in rows if 0.05 < r["wer_best"] <= THRESHOLDS["sentence_wer_max"]]
    ok = (summary["mean_wer_best"] is not None and summary["mean_wer_best"] <= THRESHOLDS["mean_wer_max"] and not flagged
          and summary["dnsmos_available"] and summary["ovrl_median"] >= THRESHOLDS["ovrl_median_min"])
    res = {"episode": ep_id, "format": fmt, "summary": summary, "thresholds": THRESHOLDS, "audio_ok": ok,
           "flagged": flagged, "minor": low_wer, "rows": rows,
           "disclaimer": "Machine evaluation on the actual synthesized audio: two-model ASR round-trip (intelligibility), DNSMOS P.835 "
                         "(perceptual quality estimate), G2P phoneme listing (pronunciation review). No human listening test was performed."}
    (out_dir / "audio-eval.json").write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    (out_dir / "audio-eval.md").write_text(render(res), encoding="utf-8")
    return res


def render(r: dict) -> str:
    s = r["summary"]
    L = [f"# Audio evaluation — {r['episode']} ({r['format']})", "", f"> {r['disclaimer']}", "",
         f"**audio_ok = {r['audio_ok']}**  •  sentences {s['sentences']}  •  models {', '.join(s['models'])}", "",
         "| metric | value | threshold |", "|---|---|---|",
         f"| mean WER (best of models) | {s['mean_wer_best']} | ≤ {r['thresholds']['mean_wer_max']} |",
         f"| mean WER base.en / small.en | {s['mean_wer_base']} / {s['mean_wer_small']} | — |",
         f"| DNSMOS OVRL median / min | {s['ovrl_median']} / {s['ovrl_min']} | median ≥ {r['thresholds']['ovrl_median_min']}, min ≥ {r['thresholds']['ovrl_sentence_min']} |",
         f"| DNSMOS SIG / BAK median | {s['sig_median']} / {s['bak_median']} | — |", ""]
    L += [f"## Flagged sentences ({len(r['flagged'])}) — WER > {r['thresholds']['sentence_wer_max']} or OVRL < {r['thresholds']['ovrl_sentence_min']}"]
    for f in r["flagged"]:
        L += [f"- [{f['scene']}] `{f['text']}`", f"  - base: `{f['hyp_base']}` (WER {f['wer_base']}) • small: `{f['hyp_small']}` (WER {f['wer_small']}) • DNSMOS {f['dnsmos']}", f"  - IPA: `{f['ipa']}`"]
    L += ["", f"## Minor ASR deviations ({len(r['minor'])}) — 0.05 < WER ≤ {r['thresholds']['sentence_wer_max']} (proper nouns, homophones)"]
    for f in r["minor"]:
        L += [f"- [{f['scene']}] WER {f['wer_best']}: `{f['text'][:90]}` → base `{(f['hyp_base'] or '')[:90]}`" + (f" • small `{f['hyp_small'][:90]}`" if f['hyp_small'] else "")]
    L += ["", "## All sentences", "| scene | dur | WER base | WER small | OVRL | SIG | BAK | text |", "|---|---|---|---|---|---|---|---|"]
    for x in r["rows"]:
        d = x["dnsmos"] or {}
        L.append(f"| {x['scene']} | {x['duration']} | {x['wer_base']} | {x['wer_small']} | {d.get('ovrl')} | {d.get('sig')} | {d.get('bak')} | {x['text'][:70]} |")
    return "\n".join(L) + "\n"
