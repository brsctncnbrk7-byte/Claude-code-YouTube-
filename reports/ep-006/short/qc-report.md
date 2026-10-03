# QC report — ep-006 (short)

**Status:** `QC_PASS`  •  technical_ok=True  •  gate_ok=True

## B. Technical checks
| check | ok | detail |
|---|---|---|
| container | ✅ | {"codec": "h264", "pix_fmt": "yuv420p", "w": 1080, "h": 1920, "fps": "30/1", "audio": "aac 48000Hz", "duration": 22.867, "frames": 686, "expected_frames": 686} |
| blackdetect | ✅ | {} |
| silencedetect | ✅ | {} |
| loudness | ✅ | {"integrated_lufs": -14.0, "true_peak_dbtp": -2.73, "lra": 6.1} |
| subtitles | ✅ | {"cues": 7, "long_or_tall": 0} |
| text_overflow | ✅ | {} |
| frame_samples | ✅ | {"count": 6, "dir": "/home/user/Claude-code-YouTube-/reports/ep-006/short/frames", "reviewed_by_claude": true} |
| frame_content | ✅ | {"blank_frames": []} |

## C. Audio evaluation (not a human listening test)
> Audio was evaluated by phoneme review, ASR round-trip and spectrogram inspection; no human listening test was performed.

**Deep evaluation on the synthesized audio: audio_ok=True** — two-model ASR mean WER best-of-models 0.0 (base.en 0.04, small.en 0.0); DNSMOS P.835 OVRL median 3.35 (min 3.24), SIG/BAK median 3.6/4.17; flagged sentences 0. Details: audio-eval.md

ASR: whisper-base.en int8 (sherpa-onnx) — mean WER **0.04**, flagged (WER>0.05): 1

- [s_compare] WER 0.2: ref=`The Digest asked the wrong people, and the wrong people answered.` hyp=`The dye just asked the wrong people, and the wrong people answered.`

<details><summary>Phoneme review (IPA per sentence)</summary>

- [s_hook] In 1936 the biggest poll in history, two point four million ballots, predicted the wrong president.
  - `ɪn nˈaɪntiːnhˈʌndɹɪd θˈɜːɾi sˈɪks ðə bˈɪɡɪst pˈoʊl ɪn hˈɪstɚɹi tˈuː pˈɔɪnt fˈɔːɹ mˈɪliən bˈæləts pɹɪdˈɪktᵻd ðə ɹˈɔŋ pɹˈɛzɪdənt`
- [s_compare] Gallup, with fifty thousand interviews chosen to mirror the country, got it right.
  - `ɡˈælʌp wɪð fˈɪfti θˈaʊzənd ˈɪntɚvjˌuːz tʃˈoʊzən tə mˈɪɹɚ ðə kˈʌntɹi ɡɑːt ɪt ɹˈaɪt`
- [s_compare] The Digest asked the wrong people, and the wrong people answered.
  - `ðə dˈaɪdʒɛst ˈæskt ðə ɹˈɔŋ pˈiːpəl ænd ðə ɹˈɔŋ pˈiːpəl ˈænsɚd`
- [s_compare] Size does not fix bias.
  - `sˈaɪz dʌznˌɑːt fˈɪks bˈaɪəs`
- [s_cta] The full story is on the channel.
  - `ðə fˈʊl stˈɔːɹi ɪz ɔnðə tʃˈænəl`

</details>

Spectrogram: `/home/user/Claude-code-YouTube-/reports/ep-006/short/spectrogram.png` (+ `_wave.png`)

## A. Content gate (manual)
| item | ok |
|---|---|
| original_narrative | ✅ |
| sources_verified | ✅ |
| visuals_explain | ✅ |
| distinct_from_previous | ✅ |
| title_thumbnail_honest | ✅ |
| ad_suitability_noted | ✅ |
| licenses_recorded | ✅ |
| frames_reviewed | ✅ |
| audio_reviewed | ✅ |

Notes: sources_verified: poll figures (10M mailed, 2.4M returned, 57/43; Gallup ~50k, 56%) and the 1936 result (60.8/36.5 → two-party 62.5/37.5) agree across the cited secondary sources; Squire (1988) and Lusinchi (2012) summaries used for the two-bias explanation; narration hedges ('later analysis found'). frames_reviewed (2026-10-03): funnel and compare_polls frames inspected — stacked bars show Landon/Roosevelt shares for Digest, Gallup and the result; labels legible. audio_reviewed: deep evaluation audio_ok (two-model ASR mean WER 0.019, DNSMOS OVRL median 3.39, 0 flagged); base-model deviations are decimal/percent renderings ('2.4 million', '24%') and proper nouns (Landon, Squire, Digest). No human listening test was performed.

Frame samples: `/home/user/Claude-code-YouTube-/reports/ep-006/short/frames` — reviewed_by_claude=True
