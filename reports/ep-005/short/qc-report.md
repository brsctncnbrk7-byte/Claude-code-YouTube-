# QC report — ep-005 (short)

**Status:** `QC_PASS_TECHNICAL_ONLY`  •  technical_ok=True  •  gate_ok=False

## B. Technical checks
| check | ok | detail |
|---|---|---|
| container | ✅ | {"codec": "h264", "pix_fmt": "yuv420p", "w": 1080, "h": 1920, "fps": "30/1", "audio": "aac 48000Hz", "duration": 26.9, "frames": 807, "expected_frames": 807} |
| blackdetect | ✅ | {} |
| silencedetect | ✅ | {} |
| loudness | ✅ | {"integrated_lufs": -14.0, "true_peak_dbtp": -2.88, "lra": 3.4} |
| subtitles | ✅ | {"cues": 7, "long_or_tall": 0} |
| text_overflow | ✅ | {} |
| frame_samples | ✅ | {"count": 6, "dir": "/home/user/Claude-code-YouTube-/reports/ep-005/short/frames", "reviewed_by_claude": false} |
| frame_content | ✅ | {"blank_frames": []} |

## C. Audio evaluation (not a human listening test)
> Audio was evaluated by phoneme review, ASR round-trip and spectrogram inspection; no human listening test was performed.

ASR: whisper-base.en int8 (sherpa-onnx) — mean WER **0.013**, flagged (WER>0.05): 1

- [s_flow] WER 0.091: ref=`In 1869 Charles Minard drew it as one band.` hyp=`In 1869, Charles Minar drew it as one band.`

<details><summary>Phoneme review (IPA per sentence)</summary>

- [s_hook] Four hundred and twenty-two thousand soldiers marched into Russia in 1812.
  - `fˈɔːɹ hˈʌndɹɪd ænd twˈɛntitˈuː θˈaʊzənd sˈoʊldʒɚz mˈɑːɹtʃt ˌɪntʊ ɹˈʌʃə ɪn wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd twˈɛlv`
- [s_hook] About ten thousand came back.
  - `ɐbˌaʊt tˈɛn θˈaʊzənd kˈeɪm bˈæk`
- [s_flow] In 1869 Charles Minard drew it as one band.
  - `ɪn wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd sˈɪksti nˈaɪn tʃˈɑːɹlz mˈaɪnɑːɹd dɹˈuː ɪɾ æz wˈʌn bˈænd`
- [s_flow] The width is the number of men.
  - `ðə wˈɪtθ ɪz ðə nˈʌmbɚɹ ʌv mˈɛn`
- [s_flow] Amber is the advance, white the retreat, and the strip below is the temperature.
  - `ˈæmbɚɹ ɪz ðɪ ɐdvˈæns wˈaɪt ðə ɹᵻtɹˈiːt ænd ðə stɹˈɪp bᵻlˌoʊ ɪz ðə tˈɛmpɹɪtʃɚ`
- [s_flow] Watch it thin to a thread.
  - `wˈɑːtʃ ɪt θˈɪn tʊ ɐ θɹˈɛd`
- [s_cta] What the map leaves out is on the channel.
  - `wˌʌt ðə mˈæp lˈiːvz ˈaʊt ɪz ɔnðə tʃˈænəl`

</details>

Spectrogram: `/home/user/Claude-code-YouTube-/reports/ep-005/short/spectrogram.png` (+ `_wave.png`)

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

Notes: Build 2 pending review.

Frame samples: `/home/user/Claude-code-YouTube-/reports/ep-005/short/frames` — reviewed_by_claude=False
