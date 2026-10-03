import pytest
from ytf.jobs import Checkpoint, with_retry, inputs_hash


def test_checkpoint_roundtrip(tmp_path):
    ck = Checkpoint(tmp_path / "ck")
    assert not ck.is_done("a", "h1")
    ck.mark("a", "h1")
    assert ck.is_done("a", "h1") and not ck.is_done("a", "h2")
    ck.clear()
    assert not ck.is_done("a", "h1")


def test_with_retry_logs_and_raises(tmp_path):
    calls = {"n": 0}

    def boom():
        calls["n"] += 1
        raise RuntimeError("x")

    with pytest.raises(RuntimeError):
        with_retry(boom, attempts=2, log=tmp_path / "err.log", label="t")
    assert calls["n"] == 2 and "attempt 2/2" in (tmp_path / "err.log").read_text()


def test_inputs_hash_changes_with_content(tmp_path):
    f = tmp_path / "a.txt"; f.write_text("1")
    h1 = inputs_hash([f]); f.write_text("2")
    assert h1 != inputs_hash([f])
