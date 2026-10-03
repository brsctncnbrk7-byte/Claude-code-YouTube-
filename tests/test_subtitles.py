from ytf.subtitles import cues_from_timeline, write_srt
from ytf.tts import SceneTiming, SentenceAudio, Timeline


def _tl():
    s1 = SentenceAudio("A short one.", "x.wav", 1.2, 0.25, 1.45)
    s2 = SentenceAudio("This is a considerably longer sentence that will certainly need to be wrapped across more than one cue block for readability.", "y.wav", 6.0, 1.8, 7.8)
    return Timeline([SceneTiming("s", 0.0, 8.5, [s1, s2])], 8.5)


def test_cues_ordered_non_overlapping(tmp_path):
    cues = cues_from_timeline(_tl())
    assert len(cues) >= 3
    for (a, b, _), (c, _, _) in zip(cues, cues[1:]):
        assert a < b <= c + 1e-9
    n = write_srt(_tl(), tmp_path / "t.srt")
    txt = (tmp_path / "t.srt").read_text()
    assert n == len(cues) and "-->" in txt and all(len(l) <= 42 for l in txt.splitlines() if l and "-->" not in l and not l.isdigit())
