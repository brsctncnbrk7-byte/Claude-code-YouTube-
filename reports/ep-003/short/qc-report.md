# QC report — ep-003 (short)

**Status:** `QC_PASS_TECHNICAL_ONLY`  •  technical_ok=True  •  gate_ok=False

## B. Technical checks
| check | ok | detail |
|---|---|---|
| container | ✅ | {"codec": "h264", "pix_fmt": "yuv420p", "w": 1080, "h": 1920, "fps": "30/1", "audio": "aac 48000Hz", "duration": 26.467, "frames": 794, "expected_frames": 794} |
| blackdetect | ✅ | {} |
| silencedetect | ✅ | {} |
| loudness | ✅ | {"integrated_lufs": -14.01, "true_peak_dbtp": -2.99, "lra": 2.6} |
| subtitles | ✅ | {"cues": 6, "long_or_tall": 0} |
| text_overflow | ✅ | {} |
| frame_samples | ✅ | {"count": 6, "dir": "/home/user/Claude-code-YouTube-/reports/ep-003/short/frames", "reviewed_by_claude": false} |
| frame_content | ✅ | {"blank_frames": []} |

## C. Audio evaluation (not a human listening test)
> Audio was evaluated by phoneme review, ASR round-trip and spectrogram inspection; no human listening test was performed.

ASR: whisper-base.en int8 (sherpa-onnx) — mean WER **0.02**, flagged (WER>0.05): 1

- [s_hook] WER 0.1: ref=`In September 1854, cholera killed one hundred and twenty-seven people in a single day in one London neighbourhood.` hyp=`In September 1854, Collara killed 127 people in a single day in one London neighborhood.`

<details><summary>Phoneme review (IPA per sentence)</summary>

- [s_hook] In September 1854, cholera killed one hundred and twenty-seven people in a single day in one London neighbourhood.
  - `ɪn sɛptˈɛmbɚ wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti fˈɔːɹ kˈɑːlɚɹə kˈɪld wˈʌn hˈʌndɹɪd ænd twˈɛntisˈɛvən pˈiːpəl ɪn ɐ sˈɪŋɡəl dˈeɪ ɪn wˈʌn lˈʌndən nˈeɪbɚhˌʊd`
- [s_handle] John Snow traced it to one water pump and had the handle removed.
  - `dʒˈɑːn snˈoʊ tɹˈeɪst ɪt tə wˈʌn wˈɔːɾɚ pˈʌmp ænd hæd ðə hˈændəl ɹᵻmˈuːvd`
- [s_handle] But look at his own data: the outbreak was already falling.
  - `bˌʌt lˈʊk æt hɪz ˈoʊn dˈeɪɾə ðɪ ˈaʊtbɹeɪk wʌz ɔːlɹˌɛdi fˈɔːlɪŋ`
- [s_handle] The handle probably stopped a second wave; the map is what proved the water did it.
  - `ðə hˈændəl pɹˈɑːbəbli stˈɑːpt ɐ sˈɛkənd wˈeɪv ðə mˈæp ɪz wʌt pɹˈuːvd ðə wˈɔːɾɚ dˈɪd ɪt`
- [s_cta] The full story, with Snow's table, is on the channel.
  - `ðə fˈʊl stˈɔːɹi wɪð snˈoʊz tˈeɪbəl ɪz ɔnðə tʃˈænəl`

</details>

Spectrogram: `/home/user/Claude-code-YouTube-/reports/ep-003/short/spectrogram.png` (+ `_wave.png`)

## A. Content gate (manual)
| item | ok |
|---|---|
| original_narrative | ✅ |
| sources_verified | ❌ |
| visuals_explain | ✅ |
| distinct_from_previous | ✅ |
| title_thumbnail_honest | ✅ |
| ad_suitability_noted | ✅ |
| licenses_recorded | ✅ |
| frames_reviewed | ❌ |
| audio_reviewed | ❌ |

Notes: Not yet built. Map geometry deliberately not reproduced (digitization license unclear); the spatial argument is told in words and with the daily tally.

Frame samples: `/home/user/Claude-code-YouTube-/reports/ep-003/short/frames` — reviewed_by_claude=False
