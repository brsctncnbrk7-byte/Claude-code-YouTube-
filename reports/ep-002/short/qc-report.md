# QC report — ep-002 (short)

**Status:** `QC_PASS`  •  technical_ok=True  •  gate_ok=True

## B. Technical checks
| check | ok | detail |
|---|---|---|
| container | ✅ | {"codec": "h264", "pix_fmt": "yuv420p", "w": 1080, "h": 1920, "fps": "30/1", "audio": "aac 48000Hz", "duration": 24.1, "frames": 723, "expected_frames": 723} |
| blackdetect | ✅ | {} |
| silencedetect | ✅ | {} |
| loudness | ✅ | {"integrated_lufs": -14.03, "true_peak_dbtp": -2.26, "lra": 2.0} |
| subtitles | ✅ | {"cues": 6, "long_or_tall": 0} |
| text_overflow | ✅ | {} |
| frame_samples | ✅ | {"count": 6, "dir": "/home/user/Claude-code-YouTube-/reports/ep-002/short/frames", "reviewed_by_claude": true} |
| frame_content | ✅ | {"blank_frames": []} |

## C. Audio evaluation (not a human listening test)
> Audio was evaluated by phoneme review, ASR round-trip and spectrogram inspection; no human listening test was performed.

ASR: whisper-base.en int8 (sherpa-onnx) — mean WER **0.0**, flagged (WER>0.05): 0


<details><summary>Phoneme review (IPA per sentence)</summary>

- [s_hook] Seventy-three seconds after launch, Challenger broke apart.
  - `sˈɛvəntiθɹˈiː sˈɛkəndz ˈæftɚ lˈɑːntʃ tʃˈælɪndʒɚ bɹˈoʊk ɐpˈɑːɹt`
- [s_hook] The night before, engineers tried to stop it with a chart.
  - `ðə nˈaɪt bᵻfˌɔːɹ ˌɛndʒɪnˈɪɹz tɹˈaɪd tə stˈɑːp ɪt wɪð ɐ tʃˈɑːɹt`
- [s_compare] They plotted only the flights with O-ring damage: no clear trend.
  - `ðeɪ plˈɑːɾᵻd ˈoʊnli ðə flˈaɪts wɪð ˈoʊɹˈɪŋ dˈæmɪdʒ nˈoʊ klˈɪɹ tɹˈɛnd`
- [s_compare] Add the sixteen flights with no damage, all of them warm, and the pattern appears.
  - `ˈæd ðə sˈɪkstiːn flˈaɪts wɪð nˈoʊ dˈæmɪdʒ ˈɔːl ʌv ðˌɛm wˈɔːɹm ænd ðə pˈætɚn ɐpˈɪɹz`
- [s_compare] Damage lives at the cold end.
  - `dˈæmɪdʒ lˈaɪvz æt ðə kˈoʊld ˈɛnd`
- [s_cta] The full story, and the model that predicted it, is on the channel.
  - `ðə fˈʊl stˈɔːɹi ænd ðə mˈɑːdəl ðæt pɹɪdˈɪktᵻd ɪɾ ɪz ɔnðə tʃˈænəl`

</details>

Spectrogram: `/home/user/Claude-code-YouTube-/reports/ep-002/short/spectrogram.png` (+ `_wave.png`)

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

Notes: sources_verified: all claims have rows in sources.md; the 23-flight table and our logistic fit are verified by computation; teleconference/temperature/caucus facts rest on secondary summaries (Rogers Commission report not readable here) and the narration avoids figures those sources disagree on. frames_reviewed (2026-10-03): Claude inspected hook, title, engineers, compare, all23, caucus frames — scatter layouts, markers (36°F, 53°F), curve and legends correct; thumbnail A readable at 320 px. audio_reviewed: ASR mean WER 0.011; the one remaining flag is the proper noun 'Thiokol' transcribed as 'Thio Call' (phonetically close; accepted). No human listening test was performed.

Frame samples: `/home/user/Claude-code-YouTube-/reports/ep-002/short/frames` — reviewed_by_claude=True
