#!/usr/bin/env python3
"""Download TTS/ASR model files from GitHub releases with sha256 verification. Idempotent.
Sources and licenses: docs/research/tools-and-licenses.md
"""
from __future__ import annotations
import hashlib, sys, tarfile, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models"
FILES = [
    # (url, target relative path, sha256 or None to record)
    ("https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1/kokoro-v1.0.onnx", "kokoro/kokoro-v1.0.onnx",
     "beb0d1848dee9a49da392cc3df26958d46cfa35d321edf434f52949153f0df3a"),
    ("https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1/voices-v1.0.bin", "kokoro/voices-v1.0.bin",
     "bca610b8308e8d99f32e6fe4197e7ec01679264efed0cac9140fe9c29f1fbf7d"),
    ("https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-base.en.tar.bz2", "asr/sherpa-onnx-whisper-base.en.tar.bz2",
     "475bc7052ce299c007f6d5d5407ba8601f819a2867f6eecee510ed17df581542"),
    # DNSMOS P.835 (Microsoft DNS-Challenge, CC BY 4.0) — QC only, never shipped in outputs
    ("https://raw.githubusercontent.com/microsoft/DNS-Challenge/master/DNSMOS/DNSMOS/sig_bak_ovr.onnx", "dnsmos/sig_bak_ovr.onnx", None),
    ("https://raw.githubusercontent.com/microsoft/DNS-Challenge/master/LICENSE", "dnsmos/LICENSE", None),
]


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def fetch(url: str, dst: Path, expect: str | None) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() and (expect is None or sha256(dst) == expect):
        print(f"ok   {dst.relative_to(ROOT)}"); return
    print(f"get  {url}")
    tmp = dst.with_suffix(dst.suffix + ".part")
    with urllib.request.urlopen(url, timeout=120) as r, open(tmp, "wb") as f:
        while chunk := r.read(1 << 20):
            f.write(chunk)
    got = sha256(tmp)
    if expect and got != expect:
        tmp.unlink(); sys.exit(f"sha256 mismatch for {dst.name}: {got} != {expect}")
    tmp.rename(dst)
    print(f"done {dst.relative_to(ROOT)} sha256={got}")


def main() -> None:
    for url, rel, expect in FILES:
        fetch(url, MODELS / rel, expect)
    tb = MODELS / "asr" / "sherpa-onnx-whisper-base.en.tar.bz2"
    d = MODELS / "asr" / "sherpa-onnx-whisper-base.en"
    if not (d / "base.en-encoder.int8.onnx").exists():
        print("extract whisper base.en")
        with tarfile.open(tb) as t:
            t.extractall(MODELS / "asr", filter="data")
    print("sha256 whisper tarball:", sha256(tb))
    print("models ready")


if __name__ == "__main__":
    main()
