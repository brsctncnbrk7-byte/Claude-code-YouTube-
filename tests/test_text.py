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
