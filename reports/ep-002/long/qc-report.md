# QC report — ep-002 (long)

**Status:** `QC_PASS`  •  technical_ok=True  •  gate_ok=True

## B. Technical checks
| check | ok | detail |
|---|---|---|
| container | ✅ | {"codec": "h264", "pix_fmt": "yuv420p", "w": 1920, "h": 1080, "fps": "30/1", "audio": "aac 48000Hz", "duration": 179.6, "frames": 5388, "expected_frames": 5388} |
| blackdetect | ✅ | {} |
| silencedetect | ✅ | {} |
| loudness | ✅ | {"integrated_lufs": -14.01, "true_peak_dbtp": -2.81, "lra": 2.4} |
| subtitles | ✅ | {"cues": 56, "long_or_tall": 0} |
| text_overflow | ✅ | {} |
| frame_samples | ✅ | {"count": 20, "dir": "/home/user/Claude-code-YouTube-/reports/ep-002/long/frames", "reviewed_by_claude": true} |
| frame_content | ✅ | {"blank_frames": []} |

## C. Audio evaluation (not a human listening test)
> Audio was evaluated by phoneme review, ASR round-trip and spectrogram inspection; no human listening test was performed.

ASR: whisper-base.en int8 (sherpa-onnx) — mean WER **0.0058**, flagged (WER>0.05): 1

- [caucus] WER 0.133: ref=`Thiokol's management took the call offline for about thirty minutes, returned, and overruled its own engineers.` hyp=`Thio Call's management took the call offline for about 30 minutes, returned, and overruled its own engineers.`

<details><summary>Phoneme review (IPA per sentence)</summary>

- [hook] Seventy-three seconds after launch, on January 28, 1986, the Space Shuttle Challenger broke apart.
  - `sˈɛvəntiθɹˈiː sˈɛkəndz ˈæftɚ lˈɑːntʃ ˌɔn dʒˈænjuːˌɛɹi twˈɛnti ˈeɪt nˈaɪntiːnhˈʌndɹɪd ˈeɪɾi sˈɪks ðə spˈeɪs ʃˈʌɾəl tʃˈælɪndʒɚ bɹˈoʊk ɐpˈɑːɹt`
- [hook] Seven people died.
  - `sˈɛvən pˈiːpəl dˈaɪd`
- [hook] The night before, a group of engineers had tried to stop the launch with a chart.
  - `ðə nˈaɪt bᵻfˌoːɹ ɐ ɡɹˈuːp ʌv ˌɛndʒɪnˈɪɹz hæd tɹˈaɪd tə stˈɑːp ðə lˈɑːntʃ wɪð ɐ tʃˈɑːɹt`
- [title] This is the story of the chart they drew, the chart they could have drawn, and the difference between them.
  - `ðɪs ɪz ðə stˈoːɹi ʌvðə tʃˈɑːɹt ðeɪ dɹˈuː ðə tʃˈɑːɹt ðeɪ kˌʊdɐv dɹˈɔːn ænd ðə dˈɪfɹəns bᵻtwˈiːn ðˌɛm`
- [engineers] On the evening of January 27, engineers at Morton Thiokol, the contractor that built the solid rocket boosters, joined a teleconference with NASA.
  - `ɔnðɪ ˈiːvnɪŋ ʌv dʒˈænjuːˌɛɹi twˈɛnti sˈɛvən ˌɛndʒɪnˈɪɹz æt mˈɔːɹtən θˌaɪoʊkˈɑːl ðə kəntɹˈæktɚ ðæt bˈɪlt ðə sˈɑːlɪd ɹˈɑːkɪt bˈuːstɚz dʒˈɔɪnd ɐ tˈɛlᵻkˌɑːnfɚɹəns wɪð nˈæsɐ`
- [engineers] Their concern was the rubber O-rings that sealed the booster joints.
  - `ðɛɹ kənsˈɜːn wʌzðə ɹˈʌbɚɹ ˈoʊɹˈɪŋz ðæt sˈiːld ðə bˈuːstɚ dʒˈɔɪnts`
- [engineers] Cold makes rubber stiff.
  - `kˈoʊld mˌeɪks ɹˈʌbɚ stˈɪf`
- [engineers] Here is the kind of evidence they had: every flight on which an O-ring had shown damage, plotted against the temperature at launch.
  - `hˈɪɹ ɪz ðə kˈaɪnd ʌv ˈɛvɪdəns ðeɪ hæd ˈɛvɹi flˈaɪt ˌɔn wˌɪtʃ ɐn ˈoʊɹˈɪŋ hæd ʃˈoʊn dˈæmɪdʒ plˈɑːɾᵻd ɐɡˈɛnst ðə tˈɛmpɹɪtʃɚɹ æt lˈɑːntʃ`
- [engineers] Seven flights.
  - `sˈɛvən flˈaɪts`
- [engineers] The coldest, at fifty-three degrees, had the most damage.
  - `ðə kˈoʊldɪst æt fˈɪftiθɹˈiː dᵻɡɹˈiːz hæd ðə mˈoʊst dˈæmɪdʒ`
- [engineers] The rest scatter from the high fifties to seventy-five.
  - `ðə ɹˈɛst skˈæɾɚ fɹʌmðə hˈaɪ fˈɪftiz tə sˈɛvəntifˈaɪv`
- [engineers] Managers looked at this and saw no clear trend.
  - `mˈænɪdʒɚz lˈʊkt æt ðɪs ænd sˈɔː nˈoʊ klˈɪɹ tɹˈɛnd`
- [compare] Now add what was left out.
  - `nˈaʊ ˈæd wʌt wʌz lˈɛft ˈaʊt`
- [compare] Sixteen flights had launched with no O-ring damage at all.
  - `sˈɪkstiːn flˈaɪts hæd lˈɑːntʃt wɪð nˈoʊ ˈoʊɹˈɪŋ dˈæmɪdʒ æɾ ˈɔːl`
- [compare] Every one of them was warm: sixty-six degrees or higher.
  - `ˈɛvɹi wˈʌn ʌv ðˌɛm wʌz wˈɔːɹm sˈɪkstisˈɪks dᵻɡɹˈiːz ɔːɹ hˈaɪɚ`
- [compare] Put the zeros back and the picture changes.
  - `pˌʊt ðə zˈiəɹoʊz bˈæk ænd ðə pˈɪktʃɚ tʃˈeɪndʒᵻz`
- [compare] Damage is not random.
  - `dˈæmɪdʒ ɪz nˌɑːt ɹˈændəm`
- [compare] It lives at the cold end.
  - `ɪt lˈɪvz æt ðə kˈoʊld ˈɛnd`
- [all23] Statisticians later fitted a simple model to these twenty-three flights: the chance that an O-ring is damaged as a function of temperature.
  - `stˌæɾɪstˈɪʃənz lˈeɪɾɚ fˈɪɾᵻd ɐ sˈɪmpəl mˈɑːdəl tə ðiːz twˈɛntiθɹˈiː flˈaɪts ðə tʃˈæns ðæt ɐn ˈoʊɹˈɪŋ ɪz dˈæmɪdʒd æz ɐ fˈʌŋkʃən ʌv tˈɛmpɹɪtʃɚ`
- [all23] Fit the same model to the public table, and the curve climbs steeply below sixty degrees.
  - `fˈɪt ðə sˈeɪm mˈɑːdəl tə ðə pˈʌblɪk tˈeɪbəl ænd ðə kˈɜːv klˈaɪmz stˈiːpli bᵻlˌoʊ sˈɪksti dᵻɡɹˈiːz`
- [all23] At fifty-three degrees, the coldest launch so far, it expects about three damaged rings out of six.
  - `æt fˈɪftiθɹˈiː dᵻɡɹˈiːz ðə kˈoʊldɪst lˈɑːntʃ sˈoʊ fˌɑːɹ ɪɾ ɛkspˈɛkts ɐbˌaʊt θɹˈiː dˈæmɪdʒd ɹˈɪŋz ˌaʊɾəv sˈɪks`
- [all23] At the thirty-six degrees recorded on the pad that morning, it expects nearly all six.
  - `æt ðə θˈɜːɾisˈɪks dᵻɡɹˈiːz ɹᵻkˈoːɹdᵻd ɔnðə pˈæd ðæt mˈɔːɹnɪŋ ɪɾ ɛkspˈɛkts nˌɪɹli ˈɔːl sˈɪks`
- [all23] The engineers' recommendation that night was to not launch below fifty-three degrees.
  - `ðɪ ˌɛndʒɪnˈɪɹz ɹˌɛkəmɛndˈeɪʃən ðæt nˈaɪt wʌz tə nˌɑːt lˈɑːntʃ bᵻlˌoʊ fˈɪftiθɹˈiː dᵻɡɹˈiːz`
- [caucus] NASA managers pushed back on the recommendation.
  - `nˈæsɐ mˈænɪdʒɚz pˈʊʃt bˈæk ɔnðə ɹˌɛkəmɛndˈeɪʃən`
- [caucus] Thiokol's management took the call offline for about thirty minutes, returned, and overruled its own engineers.
  - `θˌaɪoʊkˈɑːlz mˈænɪdʒmənt tˈʊk ðə kˈɔːl ˈɔflaɪn fɔːɹ ɐbˌaʊt θˈɜːɾi mˈɪnɪts ɹᵻtˈɜːnd ænd ˌoʊvɚɹˈuːld ɪts ˈoʊn ˌɛndʒɪnˈɪɹz`
- [caucus] The launch went ahead.
  - `ðə lˈɑːntʃ wɛnt ɐhˈɛd`
- [caucus] The Presidential Commission later traced the failure to the O-ring seal in the aft field joint of the right solid rocket booster, with cold temperature among the causes.
  - `ðə pɹˌɛzɪdˈɛnʃəl kəmˈɪʃən lˈeɪɾɚ tɹˈeɪst ðə fˈeɪlɪɹ tə ðɪ ˈoʊɹˈɪŋ sˈiːl ɪnðɪ ˈæft fˈiːld dʒˈɔɪnt ʌvðə ɹˈaɪt sˈɑːlɪd ɹˈɑːkɪt bˈuːstɚ wɪð kˈoʊld tˈɛmpɹɪtʃɚɹ ɐmˌʌŋ ðə kˈɔːzᵻz`
- [selection] The mistake has a name.
  - `ðə mɪstˈeɪk hɐz ɐ nˈeɪm`
- [selection] The engineers selected on the outcome: they plotted only the flights where damage had occurred.
  - `ðɪ ˌɛndʒɪnˈɪɹz sᵻlˈɛktᵻd ɔnðɪ ˈaʊtkʌm ðeɪ plˈɑːɾᵻd ˈoʊnli ðə flˈaɪts wˌɛɹ dˈæmɪdʒ hæd əkˈɜːd`
- [selection] That throws away the comparison group.
  - `ðæt θɹˈoʊz ɐwˈeɪ ðə kəmpˈæɹɪsən ɡɹˈuːp`
- [selection] Without the flights that went fine, there is nothing for the damaged flights to be different from.
  - `wɪðˌaʊt ðə flˈaɪts ðæt wɛnt fˈaɪn ðɛɹ ɪz nˈʌθɪŋ fɚðə dˈæmɪdʒd flˈaɪts təbi dˈɪfɹənt fɹʌm`
- [tufte] In 1989, three statisticians published a risk analysis using only the data available before the launch.
  - `ɪn nˈaɪntiːnhˈʌndɹɪd ˈeɪɾi nˈaɪn θɹˈiː stˌæɾɪstˈɪʃənz pˈʌblɪʃt ɐ ɹˈɪsk ɐnˈæləsˌɪs jˈuːzɪŋ ˈoʊnli ðə dˈeɪɾə ɐvˈeɪləbəl bᵻfˌoːɹ ðə lˈɑːntʃ`
- [tufte] Their conclusion was that the probability of failure near freezing was very high.
  - `ðɛɹ kəŋklˈuːʒən wʌz ðætðə pɹˌɑːbəbˈɪlᵻɾi ʌv fˈeɪlɪɹ nˌɪɹ fɹˈiːzɪŋ wʌz vˈɛɹi hˈaɪ`
- [tufte] Edward Tufte later made the same point about the charts themselves: the evidence existed; the display failed to show it.
  - `ˈɛdwɚd tˈʌft lˈeɪɾɚ mˌeɪd ðə sˈeɪm pˈɔɪnt ɐbˌaʊt ðə tʃˈɑːɹts ðɛmsˈɛlvz ðɪ ˈɛvɪdəns ɛɡzˈɪstᵻd ðə dɪsplˈeɪ fˈeɪld tə ʃˈoʊ ɪt`
- [why] Twenty-three rows and two columns.
  - `twˈɛntiθɹˈiː ɹˈoʊz ænd tˈuː kˈɑːlʌmz`
- [why] Shown in full, they told the truth.
  - `ʃˈoʊn ɪn fˈʊl ðeɪ tˈoʊld ðə tɹˈuːθ`
- [why] Shown in part, they said nothing at all.
  - `ʃˈoʊn ɪn pˈɑːɹt ðeɪ sˈɛd nˈʌθɪŋ æɾ ˈɔːl`
- [outro] Sources, the data table, and the model fit are in the description.
  - `sˈoːɹsᵻz ðə dˈeɪɾə tˈeɪbəl ænd ðə mˈɑːdəl fˈɪt ɑːɹ ɪnðə dᵻskɹˈɪpʃən`
- [outro] Next time: six hundred and sixteen dots, and the map that found the source of cholera.
  - `nˈɛkst tˈaɪm sˈɪks hˈʌndɹɪd ænd sˈɪkstiːn dˈɑːts ænd ðə mˈæp ðæt fˈaʊnd ðə sˈoːɹs ʌv kˈɑːlɚɹə`

</details>

Spectrogram: `/home/user/Claude-code-YouTube-/reports/ep-002/long/spectrogram.png` (+ `_wave.png`)

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

Frame samples: `/home/user/Claude-code-YouTube-/reports/ep-002/long/frames` — reviewed_by_claude=True
