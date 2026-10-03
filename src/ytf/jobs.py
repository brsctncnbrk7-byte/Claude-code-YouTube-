from __future__ import annotations
import hashlib
import json
import time
import traceback
from pathlib import Path
from typing import Callable, TypeVar

T = TypeVar("T")


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def inputs_hash(paths: list[Path], extra: str = "") -> str:
    h = hashlib.sha256()
    for p in sorted(paths):
        if p.exists():
            h.update(p.name.encode())
            h.update(sha256_file(p).encode())
    h.update(extra.encode())
    return h.hexdigest()[:16]


class Checkpoint:
    """File-based checkpoint: a step is done when `<name>.done` holds the current inputs hash."""

    def __init__(self, dir: Path):
        self.dir = dir
        self.dir.mkdir(parents=True, exist_ok=True)

    def is_done(self, name: str, h: str) -> bool:
        f = self.dir / f"{name}.done"
        return f.exists() and f.read_text().strip() == h

    def mark(self, name: str, h: str) -> None:
        (self.dir / f"{name}.done").write_text(h)

    def clear(self) -> None:
        for f in self.dir.glob("*.done"):
            f.unlink()


def with_retry(fn: Callable[[], T], attempts: int = 3, log: Path | None = None, label: str = "") -> T:
    last: Exception | None = None
    for i in range(1, attempts + 1):
        try:
            return fn()
        except Exception as e:  # noqa: BLE001
            last = e
            msg = f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {label} attempt {i}/{attempts} failed: {e!r}\n{traceback.format_exc()}\n"
            if log:
                log.parent.mkdir(parents=True, exist_ok=True)
                with open(log, "a", encoding="utf-8") as f:
                    f.write(msg)
            time.sleep(min(2 ** i, 10))
    assert last is not None
    raise last


def write_json(p: Path, obj) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


def read_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))
