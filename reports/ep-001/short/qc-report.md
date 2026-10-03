# QC report — ep-001 (short)

**Status:** `QC_PASS`  •  technical_ok=True  •  gate_ok=True

## B. Technical checks
| check | ok | detail |
|---|---|---|
| container | ✅ | {"codec": "h264", "pix_fmt": "yuv420p", "w": 1080, "h": 1920, "fps": "30/1", "audio": "aac 48000Hz", "duration": 29.967, "frames": 899, "expected_frames": 899} |
| blackdetect | ✅ | {} |
| silencedetect | ✅ | {} |
| loudness | ✅ | {"integrated_lufs": -14.03, "true_peak_dbtp": -2.45, "lra": 2.5} |
| subtitles | ✅ | {"cues": 10, "long_or_tall": 0} |
| text_overflow | ✅ | {} |
| frame_samples | ✅ | {"count": 6, "dir": "/home/user/Claude-code-YouTube-/reports/ep-001/short/frames", "reviewed_by_claude": true} |
| frame_content | ✅ | {"blank_frames": []} |

## C. Audio evaluation (not a human listening test)
> Audio was evaluated by phoneme review, ASR round-trip and spectrogram inspection; no human listening test was performed.

ASR: whisper-base.en int8 (sherpa-onnx) — mean WER **0.0**, flagged (WER>0.05): 0


<details><summary>Phoneme review (IPA per sentence)</summary>

- [s_hook] In January 1855 the British army was dying at a rate of one thousand and twenty-three men per thousand, per year.
  - `ɪn dʒˈænjuːˌɛɹi wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti fˈaɪv ðə bɹˈɪɾɪʃ ˈɑːɹmi wʌz dˈaɪɪŋ æɾɚ ɹˈeɪt ʌv wˈʌn θˈaʊzənd ænd twˈɛntiθɹˈiː mˈɛn pɜː θˈaʊzənd pɜː jˈɪɹ`
- [s_hook] Almost none of it was combat.
  - `ˈɔːlmoʊst nˈʌn ʌv ɪt wʌz kˈɑːmbæt`
- [s_rose] Florence Nightingale drew this.
  - `flˈɔːɹəns nˈaɪɾɪŋɡˌeɪl dɹˈuː ðˈɪs`
- [s_rose] Each wedge is a month.
  - `ˈiːtʃ wˈɛdʒ ɪz ɐ mˈʌnθ`
- [s_rose] Its area is the number of deaths.
  - `ɪts ˈɛɹiə ɪz ðə nˈʌmbɚɹ ʌv dˈɛθs`
- [s_rose] Blue is preventable disease.
  - `blˈuː ɪz pɹɪvˈɛntəbəl dɪzˈiːz`
- [s_rose] Red is wounds.
  - `ɹˈɛd ɪz wˈuːndz`
- [s_rose] For every soldier killed by the enemy, eight died of disease.
  - `fɔːɹ ˈɛvɹi sˈoʊldʒɚ kˈɪld baɪ ðɪ ˈɛnəmi ˈeɪt dˈaɪd ʌv dɪzˈiːz`
- [s_cta] The full story, and what the chart changed, is on the channel.
  - `ðə fˈʊl stˈɔːɹi ænd wʌt ðə tʃˈɑːɹt tʃˈeɪndʒd ɪz ɔnðə tʃˈænəl`

</details>

Spectrogram: `/home/user/Claude-code-YouTube-/reports/ep-001/short/spectrogram.png` (+ `_wave.png`)

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

Notes: sources_verified: every claim has a row in sources.md; data claims verified against the CSV, historical claims rest on secondary sources (official/primary pages unreadable from this environment) and are hedged in narration where sources differ. frames_reviewed (2026-10-03, build 2): Claude inspected hook, title, bars_all, rose_y1, rose_y2, rates, army_size, barracks, impact and the Short's s_hook/s_rose frames — layout, legends, labels and animation end-states correct; no overflow. audio_reviewed: phoneme list read for proper nouns (Nightingale, Scutari, Sevastopol, Farr, coxcomb); ASR round-trip mean WER 0.015; remaining flags are digit/word normalization ("1,758") and one ASR slip ("routine"→"routines"); spectrograms show no clipping/truncation. No human listening test was performed.

Frame samples: `/home/user/Claude-code-YouTube-/reports/ep-001/short/frames` — reviewed_by_claude=True
