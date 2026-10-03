from __future__ import annotations
import os
from pathlib import Path


def find_root(start: Path | None = None) -> Path:
    env = os.environ.get("YTF_ROOT")
    if env:
        return Path(env).resolve()
    p = (start or Path.cwd()).resolve()
    for cand in [p, *p.parents]:
        if (cand / "pyproject.toml").exists() and (cand / "src" / "ytf").exists():
            return cand
    return Path(__file__).resolve().parents[2]


ROOT = find_root()
CONTENT = ROOT / "content"
BUILD = ROOT / "build"
DIST = ROOT / "dist"
MODELS = ROOT / "models"
ASSETS = ROOT / "assets"
REPORTS = ROOT / "reports"
TEMPLATES = Path(__file__).resolve().parent / "templates"

KOKORO_MODEL = MODELS / "kokoro" / "kokoro-v1.0.onnx"
KOKORO_VOICES = MODELS / "kokoro" / "voices-v1.0.bin"
WHISPER_DIR = MODELS / "asr" / "sherpa-onnx-whisper-base.en"


def episode_dir(ep_id: str) -> Path:
    return CONTENT / ep_id


def build_dir(ep_id: str, fmt: str = "long") -> Path:
    d = BUILD / ep_id / fmt
    d.mkdir(parents=True, exist_ok=True)
    return d


def dist_dir(ep_id: str) -> Path:
    d = DIST / ep_id
    d.mkdir(parents=True, exist_ok=True)
    return d


def ensure_espeak_env() -> None:
    """Pin phonemizer/espeak to the espeak-ng bundled in the espeakng-loader wheel (identical bytes on every machine).
    Must run before any phonemizer/kokoro import. A system espeak-ng (different dictionary version) changed phonemes and
    therefore audio between otherwise identical environments — see reports/pilot/reproducibility.md (ADR-012)."""
    try:
        import espeakng_loader
    except ImportError:
        return
    data = Path(espeakng_loader.get_data_path())
    # espeak-ng stores the data path in a fixed ~160-byte buffer; longer paths are silently ignored and the library falls back
    # to its compiled-in path (then fails or another espeak gets used). Copy the data to a short path when needed.
    if len(str(data)) > 120:
        import shutil
        short = Path(os.environ.get("YTF_ESPEAK_DATA_DIR", "/tmp/ytf-espeak-ng-data"))
        marker = short / ".from"
        if not (marker.exists() and marker.read_text() == str(data)):
            if short.exists():
                shutil.rmtree(short)
            shutil.copytree(data, short)
            marker.write_text(str(data))
        data = short
    os.environ["PHONEMIZER_ESPEAK_LIBRARY"] = str(espeakng_loader.get_library_path())
    os.environ["ESPEAK_DATA_PATH"] = str(data)
