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
    """Point phonemizer at the system espeak-ng if the pip loader's data is missing."""
    lib = Path("/usr/lib/x86_64-linux-gnu/libespeak-ng.so.1")
    data = Path("/usr/lib/x86_64-linux-gnu/espeak-ng-data")
    if lib.exists():
        os.environ.setdefault("PHONEMIZER_ESPEAK_LIBRARY", str(lib))
    if data.exists():
        os.environ.setdefault("ESPEAK_DATA_PATH", str(data))
