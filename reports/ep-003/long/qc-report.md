# QC report — ep-003 (long)

**Status:** `QC_PASS`  •  technical_ok=True  •  gate_ok=True

## B. Technical checks
| check | ok | detail |
|---|---|---|
| container | ✅ | {"codec": "h264", "pix_fmt": "yuv420p", "w": 1920, "h": 1080, "fps": "30/1", "audio": "aac 48000Hz", "duration": 157.167, "frames": 4715, "expected_frames": 4715} |
| blackdetect | ✅ | {} |
| silencedetect | ✅ | {} |
| loudness | ✅ | {"integrated_lufs": -14.01, "true_peak_dbtp": -2.63, "lra": 2.3} |
| subtitles | ✅ | {"cues": 49, "long_or_tall": 0} |
| text_overflow | ✅ | {} |
| frame_samples | ✅ | {"count": 18, "dir": "/home/user/Claude-code-YouTube-/reports/ep-003/long/frames", "reviewed_by_claude": true} |
| frame_content | ✅ | {"blank_frames": []} |

## C. Audio evaluation (not a human listening test)
> Audio was evaluated by phoneme review, ASR round-trip and spectrogram inspection; no human listening test was performed.

**Deep evaluation on the synthesized audio: audio_ok=True** — two-model ASR mean WER best-of-models 0.0068 (base.en 0.0106, small.en 0.019); DNSMOS P.835 OVRL median 3.39 (min 2.92), SIG/BAK median 3.62/4.17; flagged sentences 0. Details: audio-eval.md

ASR: whisper-base.en int8 (sherpa-onnx) — mean WER **0.0106**, flagged (WER>0.05): 2

- [argument] WER 0.1: ref=`The houses that drew water from the pump suffered worst.` hyp=`The houses that drew water from the pump suffered worse.`
- [handle] WER 0.25: ref=`Look at the curve.` hyp=`Look at the curves.`

<details><summary>Phoneme review (IPA per sentence)</summary>

- [hook] On the second of September, 1854, one hundred and twenty-seven people died of cholera within a few streets of each other in Soho, London.
  - `ɔnðə sˈɛkənd ʌv sɛptˈɛmbɚ wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti fˈɔːɹ wˈʌn hˈʌndɹɪd ænd twˈɛntisˈɛvən pˈiːpəl dˈaɪd ʌv kˈɑːlɚɹə wɪðˌɪn ɐ fjˈuː stɹˈiːts ʌv ˈiːtʃ ˈʌðɚɹ ɪn sˈoʊhoʊ lˈʌndən`
- [hook] Most of them had fallen ill the day before.
  - `mˈoʊst əv ðˌɛm hæd fˈɔːlən ˈɪl ðə dˈeɪ bᵻfˈɔːɹ`
- [hook] Nobody knew what cholera was.
  - `nˈoʊbɑːdi nˈuː wʌt kˈɑːlɚɹə wʌz`
- [title] This is the story of how a doctor found the source of an epidemic with a table, a map, and a question nobody else was asking.
  - `ðɪs ɪz ðə stˈɔːɹi ʌv hˌaʊ ɐ dˈɑːktɚ fˈaʊnd ðə sˈɔːɹs əvən ˌɛpɪdˈɛmɪk wɪð ɐ tˈeɪbəl ɐ mˈæp ænd ɐ kwˈɛstʃən nˈoʊbɑːdi ˈɛls wʌz ˈæskɪŋ`
- [daily] John Snow was a physician who had argued, five years earlier, that cholera spread through water, not through bad air.
  - `dʒˈɑːn snˈoʊ wʌzɐ fɪzˈɪʃən hˌuː hæd ˈɑːɹɡjuːd fˈaɪv jˈɪɹz ˈɜːlɪɚ ðæt kˈɑːlɚɹə spɹˈɛd θɹuː wˈɔːɾɚ nˌɑːt θɹuː bˈæd ˈɛɹ`
- [daily] When the outbreak began at the end of August he went to the General Register Office and copied out the deaths, day by day.
  - `wˌɛn ðɪ ˈaʊtbɹeɪk bɪɡˈæn æt ðɪ ˈɛnd ʌv ˈɔːɡəst hiː wɛnt tə ðə dʒˈɛnɚɹəl ɹˈɛdʒɪstɚɹ ˈɑːfɪs ænd kˈɑːpɪd ˈaʊt ðə dˈɛθs dˈeɪ baɪ dˈeɪ`
- [daily] Here is his table.
  - `hˈɪɹ ɪz hɪz tˈeɪbəl`
- [daily] Almost nothing until August thirty-first.
  - `ˈɔːlmoʊst nˈʌθɪŋ ʌntˈɪl ˈɔːɡəst θˈɜːɾifˈɜːst`
- [daily] Then, in three days, hundreds.
  - `ðˈɛn ɪn θɹˈiː dˈeɪz hˈʌndɹɪdz`
- [daily] By the end of September the tally reached six hundred and sixteen.
  - `baɪ ðɪ ˈɛnd ʌv sɛptˈɛmbɚ ðə tˈæli ɹˈiːtʃt sˈɪks hˈʌndɹɪd ænd sˈɪkstiːn`
- [dots616] Six hundred and sixteen people.
  - `sˈɪks hˈʌndɹɪd ænd sˈɪkstiːn pˈiːpəl`
- [dots616] Snow walked the streets with a map and marked each death at the address where it happened.
  - `snˈoʊ wˈɔːkt ðə stɹˈiːts wɪð ɐ mˈæp ænd mˈɑːɹkt ˈiːtʃ dˈɛθ æt ðɪ ɐdɹˈɛs wˌɛɹ ɪt hˈæpənd`
- [dots616] The marks piled up around one place: the public water pump on Broad Street.
  - `ðə mˈɑːɹks pˈaɪld ˌʌp ɚɹˈaʊnd wˈʌn plˈeɪs ðə pˈʌblɪk wˈɔːɾɚ pˈʌmp ˌɔn bɹˈɔːd stɹˈiːt`
- [dots616] Streets a few minutes away, served by other pumps, were almost untouched.
  - `stɹˈiːts ɐ fjˈuː mˈɪnɪts ɐwˈeɪ sˈɜːvd baɪ ˈʌðɚ pˈʌmps wɜːɹ ˈɔːlmoʊst ʌntˈʌtʃt`
- [argument] The map made an argument.
  - `ðə mˈæp mˌeɪd ɐn ˈɑːɹɡjuːmənt`
- [argument] A workhouse near the pump had its own well, and few of its five hundred residents died.
  - `ɐ wˈɜːkhaʊs nˌɪɹ ðə pˈʌmp hæd ɪts ˈoʊn wˈɛl ænd fjˈuː ʌv ɪts fˈaɪv hˈʌndɹɪd ɹˈɛzᵻdənts dˈaɪd`
- [argument] A brewery on Broad Street gave its workers beer and had its own water; the owner reported no cases among them.
  - `ɐ bɹˈuːɚɹi ˌɔn bɹˈɔːd stɹˈiːt ɡˈeɪv ɪts wˈɜːkɚz bˈɪɹ ænd hæd ɪts ˈoʊn wˈɔːɾɚ ðɪ ˈoʊnɚ ɹᵻpˈɔːɹɾᵻd nˈoʊ kˈeɪsᵻz ɐmˈʌŋ ðˌɛm`
- [argument] The houses that drew water from the pump suffered worst.
  - `ðə hˈaʊzᵻz ðæt dɹˈuː wˈɔːɾɚ fɹʌmðə pˈʌmp sˈʌfɚd wˈɜːst`
- [argument] The pattern followed the water, not the air.
  - `ðə pˈætɚn fˈɑːloʊd ðə wˈɔːɾɚ nˌɑːt ðɪ ˈɛɹ`
- [handle] On the evening of September seventh Snow presented his evidence to the parish Board of Guardians.
  - `ɔnðɪ ˈiːvnɪŋ ʌv sɛptˈɛmbɚ sˈɛvənθ snˈoʊ pɹɪzˈɛntᵻd hɪz ˈɛvɪdəns tə ðə pˈæɹɪʃ bˈɔːɹd ʌv ɡˈɑːɹdiənz`
- [handle] The next day the pump handle was removed.
  - `ðə nˈɛkst dˈeɪ ðə pˈʌmp hˈændəl wʌz ɹᵻmˈuːvd`
- [handle] Here is the part the legend leaves out.
  - `hˈɪɹ ɪz ðə pˈɑːɹt ðə lˈɛdʒənd lˈiːvz ˈaʊt`
- [handle] Look at the curve.
  - `lˈʊk æt ðə kˈɜːv`
- [handle] New cases had peaked on September first.
  - `nˈuː kˈeɪsᵻz hæd pˈiːkt ˌɔn sɛptˈɛmbɚ fˈɜːst`
- [handle] By the eighth, deaths had already fallen from one hundred and twenty-seven a day to thirty.
  - `baɪ ðɪ ˈeɪtθ dˈɛθs hæd ɔːlɹˌɛdi fˈɔːlən fɹʌm wˈʌn hˈʌndɹɪd ænd twˈɛntisˈɛvən ɐ dˈeɪ tə θˈɜːɾi`
- [handle] The outbreak was ending on its own, partly because so many people had fled.
  - `ðɪ ˈaʊtbɹeɪk wʌz ˈɛndɪŋ ˌɔn ɪts ˈoʊn pˈɑːɹtli bɪkˈʌz sˌoʊ mˈɛni pˈiːpəl hæd flˈɛd`
- [whitehead] So did the handle matter?
  - `sˌoʊ dˈɪd ðə hˈændəl mˈæɾɚ`
- [whitehead] It almost certainly prevented a second wave, and it mattered for another reason.
  - `ɪɾ ˈɔːlmoʊst sˈɜːʔn̩li pɹɪvˈɛntᵻd ɐ sˈɛkənd wˈeɪv ænd ɪt mˈæɾɚd fɔːɹ ɐnˈʌðɚ ɹˈiːzən`
- [whitehead] A local curate, Henry Whitehead, did not believe Snow.
  - `ɐ lˈoʊkəl kjˈʊɹɹeɪt hˈɛnɹi wˈaɪthɛd dɪdnˌɑːt bᵻlˈiːv snˈoʊ`
- [whitehead] He set out to disprove him by re-interviewing the parish, house by house.
  - `hiː sˈɛt ˈaʊt tə dɪspɹˈuːv hˌɪm baɪ ɹˌiːˈɪntɚvjˌuːɪŋ ðə pˈæɹɪʃ hˈaʊs baɪ hˈaʊs`
- [whitehead] Instead he found the first case: an infant whose washing water had been emptied into a cesspit a few feet from the pump's well.
  - `ɪnstˈɛd hiː fˈaʊnd ðə fˈɜːst kˈeɪs ɐn ˈɪnfənt hˌuːz wˈɑːʃɪŋ wˈɔːɾɚ hɐdbɪn ˈɛmptid ˌɪntʊ ɐ sˈɛspɪt ɐ fjˈuː fˈiːt fɹʌmðə pˈʌmps wˈɛl`
- [lesson] Snow never saw the bacterium.
  - `snˈoʊ nˈɛvɚ sˈɔː ðə bæktˈɪɹiəm`
- [lesson] It would be identified decades later.
  - `ɪt wʊd biː aɪdˈɛntᵻfˌaɪd dˈɛkeɪdz lˈeɪɾɚ`
- [lesson] What he had was a count over time, a map over space, and comparison groups: the workhouse, the brewery, the people who drank elsewhere.
  - `wˌʌt hiː hæd wʌzɐ kˈaʊnt ˌoʊvɚ tˈaɪm ɐ mˈæp ˌoʊvɚ spˈeɪs ænd kəmpˈæɹɪsən ɡɹˈuːps ðə wˈɜːkhaʊs ðə bɹˈuːɚɹi ðə pˈiːpəl hˌuː dɹˈæŋk ˈɛlswɛɹ`
- [lesson] That is still how outbreaks are traced.
  - `ðæt ɪz stˈɪl hˌaʊ ˈaʊtbɹeɪks ɑːɹ tɹˈeɪst`
- [outro] Snow's table and the sources for this episode are in the description.
  - `snˈoʊz tˈeɪbəl ænd ðə sˈɔːɹsᵻz fɔːɹ ðɪs ˈɛpɪsˌoʊd ɑːɹ ɪnðə dᵻskɹˈɪpʃən`
- [outro] Next time: the bombers that came back, and the holes that were not there.
  - `nˈɛkst tˈaɪm ðə bˈɑːmɚz ðæt kˈeɪm bˈæk ænd ðə hˈoʊlz ðæt wɜː nˌɑːt ðˈɛɹ`

</details>

Spectrogram: `/home/user/Claude-code-YouTube-/reports/ep-003/long/spectrogram.png` (+ `_wave.png`)

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

Notes: sources_verified: daily table verified against CSV (616 deaths, 127 on Sept 2, 30 on Sept 8); historical claims rest on secondary summaries (CDC MMWR, Wikipedia, PMC) and are hedged ('by one widely repeated account' style wording where needed); Snow's 'date unknown' row (45 attacks, 0 deaths) is excluded from the time charts and noted here. frames_reviewed (2026-10-03): Claude inspected daily, dots616 (616 dots; Sept 8 onward highlighted), handle (Sept 8 marker; curve already falling) — correct after removing the undated row that produced a spurious end spike. audio_reviewed: ASR mean WER 0.039 before ordinal normalization; flags were ordinals (2nd/31st/7th/1st/8th), 'Snow's', and ASR slips (worst→worse, curve→curves, cholera→Collara in the Short); phonemes for Soho, Whitehead, cholera, cesspit checked. No human listening test was performed. Map geometry deliberately not reproduced (digitization license unclear); the spatial argument is told in words and with the daily tally.

Frame samples: `/home/user/Claude-code-YouTube-/reports/ep-003/long/frames` — reviewed_by_claude=True
