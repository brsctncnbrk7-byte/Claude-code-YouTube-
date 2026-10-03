"""ytf — Plotted Past production pipeline (free, CPU-only)."""
__version__ = "0.1.0"

from .paths import ensure_espeak_env as _ensure_espeak_env

_ensure_espeak_env()  # pin espeak-ng before phonemizer/kokoro are imported anywhere
