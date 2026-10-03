from ytf.text import split_sentences, wrap_lines, wer


def test_split_sentences_basic():
    s = split_sentences("In 1854, a map was drawn. On it, he marked deaths. Was it true? Yes!")
    assert s == ["In 1854, a map was drawn.", "On it, he marked deaths.", "Was it true?", "Yes!"]


def test_split_keeps_abbreviations():
    s = split_sentences("Dr. Snow drew it. St. James parish counted 616 deaths.")
    assert len(s) == 2 and s[0].startswith("Dr. Snow")


def test_wrap_lines_limits():
    blocks = wrap_lines("word " * 30, max_chars=42, max_lines=2)
    assert all(len(l) <= 42 for b in blocks for l in b)
    assert all(len(b) <= 2 for b in blocks)


def test_wer():
    assert wer("the cat sat", "the cat sat") == 0.0
    assert abs(wer("the cat sat", "the cat") - 1 / 3) < 1e-9


def test_tts_deterministic_when_models_present(tmp_path):
    """Seeded per-sentence sessions must give bit-identical audio (ADR-012). Skipped when models are absent."""
    import pytest
    from ytf import paths
    if not paths.KOKORO_MODEL.exists():
        pytest.skip("kokoro model not downloaded")
    import numpy as np, soundfile as sf
    from ytf.tts import synth_sentence
    a = synth_sentence("Determinism check, one two three.", "af_heart", 1.0, "en-us", tmp_path / "a")
    b = synth_sentence("Determinism check, one two three.", "af_heart", 1.0, "en-us", tmp_path / "b")
    x, y = sf.read(a.wav)[0], sf.read(b.wav)[0]
    assert len(x) == len(y) and np.array_equal(x, y)


def test_respelling_split():
    from ytf.tts import display_text, spoken_text
    t = "Zero degrees [[Réaumur|Ray-oh-mur]] on October eighteenth."
    assert display_text(t) == "Zero degrees Réaumur on October eighteenth."
    assert spoken_text(t) == "Zero degrees Ray-oh-mur on October eighteenth."
