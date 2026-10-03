from __future__ import annotations
import json
from dataclasses import dataclass, asdict
from pathlib import Path
import numpy as np
import soundfile as sf

from . import paths
from .jobs import sha256_text
from .text import split_sentences

SR = 24000
SENTENCE_GAP = 0.35
_synth = None


def get_synth():
    global _synth
    if _synth is None:
        paths.ensure_espeak_env()
        from kokoro_onnx import Kokoro  # heavy import, lazy
        if not paths.KOKORO_MODEL.exists() or not paths.KOKORO_VOICES.exists():
            raise FileNotFoundError("Kokoro model files missing; run `uv run python scripts/fetch_models.py`")
        _synth = Kokoro(str(paths.KOKORO_MODEL), str(paths.KOKORO_VOICES))
    return _synth


def list_voices() -> list[str]:
    return sorted(get_synth().get_voices())


@dataclass
class SentenceAudio:
    text: str
    wav: str
    duration: float
    start: float = 0.0  # filled by timeline
    end: float = 0.0


def synth_sentence(text: str, voice: str, speed: float, lang: str, cache_dir: Path) -> SentenceAudio:
    cache_dir.mkdir(parents=True, exist_ok=True)
    key = sha256_text(f"kokoro-v1.0|{voice}|{speed}|{lang}|{text}")[:20]
    wav = cache_dir / f"{key}.wav"
    meta = cache_dir / f"{key}.json"
    if wav.exists() and meta.exists():
        m = json.loads(meta.read_text())
        return SentenceAudio(text, str(wav), m["duration"])
    samples, sr = get_synth().create(text, voice=voice, speed=speed, lang=lang)
    samples = np.asarray(samples, dtype=np.float32)
    # trim leading/trailing silence below -50 dBFS, keep 60 ms margins
    thr = 10 ** (-50 / 20)
    idx = np.where(np.abs(samples) > thr)[0]
    if len(idx):
        a = max(0, idx[0] - int(0.06 * sr))
        b = min(len(samples), idx[-1] + int(0.06 * sr))
        samples = samples[a:b]
    sf.write(wav, samples, sr)
    dur = len(samples) / sr
    meta.write_text(json.dumps({"text": text, "voice": voice, "speed": speed, "lang": lang, "duration": dur, "sr": sr}))
    return SentenceAudio(text, str(wav), dur)


@dataclass
class SceneTiming:
    id: str
    start: float
    end: float
    sentences: list[SentenceAudio]

    @property
    def duration(self) -> float:
        return self.end - self.start


@dataclass
class Timeline:
    scenes: list[SceneTiming]
    total: float
    sr: int = SR

    def to_json(self) -> dict:
        return {
            "total": self.total,
            "sr": self.sr,
            "scenes": [
                {"id": s.id, "start": s.start, "end": s.end, "sentences": [asdict(x) for x in s.sentences]}
                for s in self.scenes
            ],
        }

    @staticmethod
    def from_json(d: dict) -> "Timeline":
        return Timeline(
            scenes=[SceneTiming(s["id"], s["start"], s["end"], [SentenceAudio(**x) for x in s["sentences"]]) for s in d["scenes"]],
            total=d["total"], sr=d.get("sr", SR),
        )


def build_narration(scenes, voice: str, speed: float, lang: str, out_dir: Path, fps: int = 30) -> Timeline:
    """Synthesize every sentence, lay them on a timeline, write narration_raw.wav (24 kHz mono float)."""
    cache = paths.BUILD / "_tts_cache"
    t = 0.0
    timings: list[SceneTiming] = []
    chunks: list[tuple[float, np.ndarray]] = []
    for sc in scenes:
        start = t
        sents = []
        t += 0.25  # small lead-in per scene
        for s in split_sentences(sc.narration):
            sa = synth_sentence(s, voice, speed, lang, cache)
            data, sr = sf.read(sa.wav, dtype="float32")
            sa.start, sa.end = t, t + sa.duration
            chunks.append((t, data))
            sents.append(sa)
            t = sa.end + SENTENCE_GAP
        if sents:
            t = t - SENTENCE_GAP + sc.pad_after
        end = max(start + sc.min_duration, t)
        # snap scene end to frame grid so video frames == audio length
        end = round(end * fps) / fps
        t = end
        timings.append(SceneTiming(sc.id, start, end, sents))
    total = t
    audio = np.zeros(int(round(total * SR)) + 1, dtype=np.float32)
    for st, data in chunks:
        i = int(round(st * SR))
        audio[i:i + len(data)] += data[: len(audio) - i]
    peak = float(np.abs(audio).max()) if len(audio) else 0.0
    if peak > 0.98:
        audio = audio * (0.98 / peak)
    out_dir.mkdir(parents=True, exist_ok=True)
    sf.write(out_dir / "narration_raw.wav", audio, SR)
    tl = Timeline(timings, total)
    (out_dir / "timeline.json").write_text(json.dumps(tl.to_json(), indent=2))
    return tl


def phonemes_for(sentences: list[str], lang: str = "en-us") -> list[str]:
    """IPA from the same G2P stack kokoro-onnx uses (espeak via phonemizer) — for pre-synthesis review."""
    paths.ensure_espeak_env()
    from phonemizer import phonemize
    return [phonemize(s, language=lang, backend="espeak", with_stress=True, strip=True) for s in sentences]
