# QC report — ep-001 (long)

**Status:** `QC_FAIL`  •  technical_ok=False  •  gate_ok=False

## B. Technical checks
| check | ok | detail |
|---|---|---|
| container | ✅ | {"codec": "h264", "pix_fmt": "yuv420p", "w": 1920, "h": 1080, "fps": "30/1", "audio": "aac 48000Hz", "duration": 287.867, "frames": 8636, "expected_frames": 8636} |
| blackdetect | ❌ | {} events=5 |
| silencedetect | ✅ | {} |
| loudness | ✅ | {"integrated_lufs": -14.02, "true_peak_dbtp": -2.52, "lra": 2.4} |
| subtitles | ✅ | {"cues": 81, "long_or_tall": 0} |
| text_overflow | ✅ | {} |
| frame_samples | ✅ | {"count": 28, "dir": "/home/user/Claude-code-YouTube-/reports/ep-001/long/frames", "reviewed_by_claude": false} |

## C. Audio evaluation (not a human listening test)
> Audio was evaluated by phoneme review, ASR round-trip and spectrogram inspection; no human listening test was performed.

ASR: whisper-base.en int8 (sherpa-onnx) — mean WER **0.0145**, flagged (WER>0.05): 3

- [bars_all] WER 0.5: ref=`Wounds killed one thousand seven hundred and fifty-eight.` hyp=`Wounds killed 1,758.`
- [army_size] WER 0.176: ref=`In April 1854 there were about eight and a half thousand British soldiers in the East.` hyp=`In April 1854, there were about 8,500 British soldiers in the east.`
- [impact] WER 0.083: ref=`Reforms followed: an army medical school, routine sanitary statistics for barracks and hospitals.` hyp=`Reforms followed. An Army medical school routines sanitary statistics for barracks and hospitals.`

<details><summary>Phoneme review (IPA per sentence)</summary>

- [hook] In January 1855, the British army besieging Sevastopol was dying at a rate of one thousand and twenty-three men per thousand, per year.
  - `ɪn dʒˈænjuːˌɛɹi wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti fˈaɪv ðə bɹˈɪɾɪʃ ˈɑːɹmi bᵻsˈiːdʒɪŋ sˈɛvɐstˌɑːpɑːl wʌz dˈaɪɪŋ æɾɚ ɹˈeɪt ʌv wˈʌn θˈaʊzənd ænd twˈɛntiθɹˈiː mˈɛn pɜː θˈaʊzənd pɜː jˈɪɹ`
- [hook] Read that again.
  - `ɹˈiːd ðæt ɐɡˈɛn`
- [hook] At that rate, disease alone would have wiped out the entire army in under a year, without the enemy firing a shot.
  - `æt ðæt ɹˈeɪt dɪzˈiːz ɐlˈoʊn wʊdhɐv wˈaɪpt ˈaʊt ðɪ ɛntˈaɪɚɹ ˈɑːɹmi ɪn ˌʌndɚɹ ɐ jˈɪɹ wɪðˌaʊt ðɪ ˈɛnəmi fˈaɪɚɹɪŋ ɐ ʃˈɑːt`
- [title] This is the story of how one woman turned that ledger into a picture, and why the picture worked where the numbers had failed.
  - `ðɪs ɪz ðə stˈoːɹi ʌv hˌaʊ wˈʌn wˈʊmən tˈɜːnd ðæt lˈɛdʒɚɹ ˌɪntʊ ɐ pˈɪktʃɚ ænd wˌaɪ ðə pˈɪktʃɚ wˈɜːkt wˌɛɹ ðə nˈʌmbɚz hæd fˈeɪld`
- [bars_all] Here is every month of the war, from April 1854 to March 1856.
  - `hˈɪɹ ɪz ˈɛvɹi mˈʌnθ ʌvðə wˈɔːɹ fɹʌm ˈeɪpɹəl wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti fˈoːɹ tə mˈɑːɹtʃ wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti sˈɪks`
- [bars_all] Blue is death from disease: cholera, typhus, dysentery.
  - `blˈuː ɪz dˈɛθ fɹʌm dɪzˈiːz kˈɑːlɚɹə tˈaɪfəs dˈɪsəntɚɹi`
- [bars_all] Red is death from wounds.
  - `ɹˈɛd ɪz dˈɛθ fɹʌm wˈuːndz`
- [bars_all] White is everything else.
  - `wˈaɪt ɪz ˈɛvɹɪθˌɪŋ ˈɛls`
- [bars_all] The bars are not close.
  - `ðə bˈɑːɹz ɑːɹ nˌɑːt klˈoʊs`
- [bars_all] Over the whole war, disease killed fourteen thousand four hundred and seventy-six British soldiers.
  - `ˌoʊvɚ ðə hˈoʊl wˈɔːɹ dɪzˈiːz kˈɪld fˈoːɹtiːn θˈaʊzənd fˈoːɹ hˈʌndɹɪd ænd sˈɛvəntisˈɪks bɹˈɪɾɪʃ sˈoʊldʒɚz`
- [bars_all] Wounds killed one thousand seven hundred and fifty-eight.
  - `wˈuːndz kˈɪld wˈʌn θˈaʊzənd sˈɛvən hˈʌndɹɪd ænd fˈɪftiˈeɪt`
- [bars_all] For every soldier killed by the enemy, eight died of something that could have been prevented.
  - `fɔːɹ ˈɛvɹi sˈoʊldʒɚ kˈɪld baɪ ðɪ ˈɛnəmi ˈeɪt dˈaɪd ʌv sˈʌmθɪŋ ðæt kˌʊdɐv bˌɪn pɹɪvˈɛntᵻd`
- [ledger] The numbers came from army returns, compiled with William Farr, the statistician at the General Register Office.
  - `ðə nˈʌmbɚz kˈeɪm fɹʌm ˈɑːɹmi ɹᵻtˈɜːnz kəmpˈaɪld wɪð wˈɪljəm fˈɑːɹ ðə stˌæɾɪstˈɪʃən æt ðə dʒˈɛnɚɹəl ɹˈɛdʒɪstɚɹ ˈɑːfɪs`
- [ledger] Florence Nightingale reached the barracks hospital at Scutari in November 1854 and found the record keeping in disarray.
  - `flˈɔːɹəns nˈaɪɾɪŋɡˌeɪl ɹˈiːtʃt ðə bˈɛɹəks hˈɑːspɪɾəl æt skjuːtˈɑːɹɹi ɪn noʊvˈɛmbɚ wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti fˈoːɹ ænd fˈaʊnd ðə ɹˈɛkɚd kˈiːpɪŋ ɪn dˌɪsɚɹˈeɪ`
- [ledger] She sorted every death into three columns: zymotic disease, meaning epidemic and preventable; wounds; and everything else.
  - `ʃiː sˈɔːɹɾᵻd ˈɛvɹi dˈɛθ ˌɪntʊ θɹˈiː kˈɑːlʌmz zaɪmˈɑːɾɪk dɪzˈiːz mˈiːnɪŋ ˌɛpɪdˈɛmɪk ænd pɹɪvˈɛntəbəl wˈuːndz ænd ˈɛvɹɪθˌɪŋ ˈɛls`
- [ledger] Counting came before cleaning.
  - `kˈaʊntɪŋ kˈeɪm bᵻfˌoːɹ klˈiːnɪŋ`
- [rose_y1] In 1858 she drew this.
  - `ɪn wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti ˈeɪt ʃiː dɹˈuː ðˈɪs`
- [rose_y1] Twelve wedges, one per month, starting in April 1854 and running clockwise.
  - `twˈɛlv wˈɛdʒᵻz wˈʌn pɜː mˈʌnθ stˈɑːɹɾɪŋ ɪn ˈeɪpɹəl wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti fˈoːɹ ænd ɹˈʌnɪŋ klˈɑːkwaɪz`
- [rose_y1] The area of each wedge, not its length, is proportional to the number of deaths.
  - `ðɪ ˈɛɹiə ʌv ˈiːtʃ wˈɛdʒ nˌɑːt ɪts lˈɛŋθ ɪz pɹəpˈoːɹʃənəl tə ðə nˈʌmbɚɹ ʌv dˈɛθs`
- [rose_y1] Blue is preventable disease.
  - `blˈuː ɪz pɹɪvˈɛntəbəl dɪzˈiːz`
- [rose_y1] Red is wounds.
  - `ɹˈɛd ɪz wˈuːndz`
- [rose_y1] White is other causes.
  - `wˈaɪt ɪz ˈʌðɚ kˈɔːzᵻz`
- [rose_y1] Watch what happens as winter arrives.
  - `wˈɑːtʃ wʌt hˈæpənz æz wˈɪntɚɹ ɚɹˈaɪvz`
- [rose_y1] Watch January.
  - `wˈɑːtʃ dʒˈænjuːˌɛɹi`
- [rose_y2] Now the second year, drawn at exactly the same scale.
  - `nˈaʊ ðə sˈɛkənd jˈɪɹ dɹˈɔːn æɾ ɛɡzˈæktli ðə sˈeɪm skˈeɪl`
- [rose_y2] In March 1855 a Sanitary Commission reached Scutari.
  - `ɪn mˈɑːɹtʃ wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti fˈaɪv ɐ sˈænətˌɛɹi kəmˈɪʃən ɹˈiːtʃt skjuːtˈɑːɹɹi`
- [rose_y2] It flushed the sewers, cleared the latrines, and, by one widely repeated account, removed a dead horse from the water supply.
  - `ɪt flˈʌʃt ðə sˈuːɚz klˈɪɹd ðə lɐtɹˈiːnz ænd baɪ wˈʌn wˈaɪdli ɹᵻpˈiːɾᵻd ɐkˈaʊnt ɹᵻmˈuːvd ɐ dˈɛd hˈɔːɹs fɹʌmðə wˈɔːɾɚ səplˈaɪ`
- [rose_y2] The wedges shrink.
  - `ðə wˈɛdʒᵻz ʃɹˈɪŋk`
- [rose_y2] By September 1855, for the first time, more soldiers died of wounds than of disease.
  - `baɪ sɛptˈɛmbɚ wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti fˈaɪv fɚðə fˈɜːst tˈaɪm mˈoːɹ sˈoʊldʒɚz dˈaɪd ʌv wˈuːndz ðɐn ʌv dɪzˈiːz`
- [army_size] One more thing the table shows.
  - `wˈʌn mˈoːɹ θˈɪŋ ðə tˈeɪbəl ʃˈoʊz`
- [army_size] The army itself was changing.
  - `ðɪ ˈɑːɹmi ɪtsˈɛlf wʌz tʃˈeɪndʒɪŋ`
- [army_size] In April 1854 there were about eight and a half thousand British soldiers in the East.
  - `ɪn ˈeɪpɹəl wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti fˈoːɹ ðɛɹwˌɜːɹ ɐbˌaʊt ˈeɪt ænd ɐ hˈæf θˈaʊzənd bɹˈɪɾɪʃ sˈoʊldʒɚz ɪnðɪ ˈiːst`
- [army_size] By March 1856 there were more than forty-six thousand.
  - `baɪ mˈɑːɹtʃ wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti sˈɪks ðɛɹwˌɜː mˈoːɹ ðɐn fˈɔːɹɾisˈɪks θˈaʊzənd`
- [army_size] A death count in a small army and a death count in a large one are not the same thing, which is why Nightingale, following Farr, reported deaths as annual rates per thousand.
  - `ɐ dˈɛθ kˈaʊnt ɪn ɐ smˈɔːl ˈɑːɹmi ænd ɐ dˈɛθ kˈaʊnt ɪn ɐ lˈɑːɹdʒ wˈʌn ɑːɹ nˌɑːt ðə sˈeɪm θˈɪŋ wˌɪtʃ ɪz wˌaɪ nˈaɪɾɪŋɡˌeɪl fˈɑːloʊɪŋ fˈɑːɹ ɹᵻpˈoːɹɾᵻd dˈɛθs æz ˈænjuːəl ɹˈeɪts pɜː θˈaʊzənd`
- [rates] Rates tell the same story with the army's size taken out.
  - `ɹˈeɪts tˈɛl ðə sˈeɪm stˈoːɹi wɪððɪ ˈɑːɹmiz sˈaɪz tˈeɪkən ˈaʊt`
- [rates] The army more than doubled during the war, so raw counts can mislead.
  - `ðɪ ˈɑːɹmi mˈoːɹ ðɐn dˈʌbəld dˈʊɹɹɪŋ ðə wˈɔːɹ sˌoʊ ɹˈɔː kˈaʊnts kæn mɪslˈiːd`
- [rates] Per thousand men, disease deaths fell from over one thousand a year in January 1855 to under four by March 1856.
  - `pɜː θˈaʊzənd mˈɛn dɪzˈiːz dˈɛθs fˈɛl fɹʌm ˌoʊvɚ wˈʌn θˈaʊzənd ɐ jˈɪɹ ɪn dʒˈænjuːˌɛɹi wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti fˈaɪv tʊ ˌʌndɚ fˈoːɹ baɪ mˈɑːɹtʃ wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti sˈɪks`
- [batswing] Her first attempt, later nicknamed the bat's wing, scaled the radius of each wedge to the death rate.
  - `hɜː fˈɜːst ɐtˈɛmpt lˈeɪɾɚ nˈɪkneɪmd ðə bˈæts wˈɪŋ skˈeɪld ðə ɹˈeɪdɪəs ʌv ˈiːtʃ wˈɛdʒ tə ðə dˈɛθ ɹˈeɪt`
- [batswing] That exaggerates: double the deaths looks like four times the area.
  - `ðæt ɛɡzˈædʒɚɹˌeɪts dˈʌbəl ðə dˈɛθs lˈʊks lˈaɪk fˈoːɹ tˈaɪmz ðɪ ˈɛɹiə`
- [batswing] She redrew it so that the area of each wedge carried the number, and wrote the rule into the legend itself.
  - `ʃiː ɹiːdɹˈuː ɪt sˌoʊ ðætðɪ ˈɛɹiə ʌv ˈiːtʃ wˈɛdʒ kˈæɹid ðə nˈʌmbɚ ænd ɹˈoʊt ðə ɹˈuːl ˌɪntʊ ðə lˈɛdʒənd ɪtsˈɛlf`
- [coxcomb] Most people call the chart a coxcomb.
  - `mˈoʊst pˈiːpəl kˈɔːl ðə tʃˈɑːɹt ɐ kˈɑːkskoʊm`
- [coxcomb] According to historian Hugh Small, she used that word for the printed booklet the diagrams appeared in, not for the chart itself.
  - `ɐkˈoːɹdɪŋ tə hɪstˈoːɹiən hjˈuː smˈɔːl ʃiː jˈuːzd ðæt wˈɜːd fɚðə pɹˈɪntᵻd bˈʊklɪt ðə dˈaɪəɡɹˌæmz ɐpˈɪɹd ɪn nˌɑːt fɚðə tʃˈɑːɹt ɪtsˈɛlf`
- [barracks] She did not stop at the war.
  - `ʃiː dɪdnˌɑːt stˈɑːp æt ðə wˈɔːɹ`
- [barracks] Back in England she compared young soldiers living in barracks with civilian men of the same ages.
  - `bˈæk ɪn ˈɪŋɡlənd ʃiː kəmpˈɛɹd jˈʌŋ sˈoʊldʒɚz lˈɪvɪŋ ɪn bˈɛɹəks wɪð sɪvˈɪliən mˈɛn ʌvðə sˈeɪm ˈeɪdʒᵻz`
- [barracks] Civilians died at about eleven per thousand a year.
  - `sɪvˈɪliənz dˈaɪd æɾ ɐbˌaʊt ᵻlˈɛvən pɜː θˈaʊzənd ɐ jˈɪɹ`
- [barracks] Infantry, seventeen.
  - `ˈɪnfəntɹi sˈɛvəntˌiːn`
- [barracks] Artillery, nineteen.
  - `ɑːɹtˈɪlɚɹi nˈaɪntiːn`
- [barracks] Guards, twenty.
  - `ɡˈɑːɹdz twˈɛnti`
- [barracks] Healthy men, already screened by a medical exam, were dying at nearly twice the civilian rate in peacetime.
  - `hˈɛlθi mˈɛn ɔːlɹˌɛdi skɹˈiːnd baɪ ɐ mˈɛdɪkəl ɛɡzˈæm wɜː dˈaɪɪŋ æt nˌɪɹli twˈaɪs ðə sɪvˈɪliən ɹˈeɪt ɪn pˈiːstaɪm`
- [barracks] She printed two thousand copies of the report at her own expense and sent them to people who could act.
  - `ʃiː pɹˈɪntᵻd tˈuː θˈaʊzənd kˈɑːpɪz ʌvðə ɹᵻpˈoːɹt æt hɜːɹ ˈoʊn ɛkspˈɛns ænd sˈɛnt ðˌɛm tə pˈiːpəl hˌuː kʊd ˈækt`
- [impact] The diagram went into her evidence for the Royal Commission on the Health of the Army, formed in 1857, and to the people who could act: Queen Victoria, Sidney Herbert, members of Parliament.
  - `ðə dˈaɪəɡɹˌæm wɛnt ˌɪntʊ hɜːɹ ˈɛvɪdəns fɚðə ɹˈɔɪəl kəmˈɪʃən ɔnðə hˈɛlθ ʌvðɪ ˈɑːɹmi fˈɔːɹmd ɪn wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti sˈɛvən ænd tə ðə pˈiːpəl hˌuː kʊd ˈækt kwˈiːn vɪktˈoːɹiə sˈɪdni hˈɜːbɚt mˈɛmbɚz ʌv pˈɑːɹləmənt`
- [impact] Reforms followed: an army medical school, routine sanitary statistics for barracks and hospitals.
  - `ɹᵻfˈɔːɹmz fˈɑːloʊd ɐn ˈɑːɹmi mˈɛdɪkəl skˈuːl ɹuːtˈiːn sˈænətˌɛɹi stɐtˈɪstɪks fɔːɹ bˈɛɹəks ænd hˈɑːspɪɾəlz`
- [impact] In 1858 she became the first woman elected to the Statistical Society of London.
  - `ɪn wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd fˈɪfti ˈeɪt ʃiː bɪkˌeɪm ðə fˈɜːst wˈʊmən ᵻlˈɛktᵻd tə ðə stɐtˈɪstɪkəl səsˈaɪəɾi ʌv lˈʌndən`
- [why] The report had hundreds of pages of tables.
  - `ðə ɹᵻpˈoːɹt hæd hˈʌndɹɪdz ʌv pˈeɪdʒᵻz ʌv tˈeɪbəlz`
- [why] The chart made one argument, and made it in a shape: the biggest killer was the one you could fix.
  - `ðə tʃˈɑːɹt mˌeɪd wˈʌn ˈɑːɹɡjuːmənt ænd mˌeɪd ɪɾ ɪn ɐ ʃˈeɪp ðə bˈɪɡɪst kˈɪlɚ wʌzðə wˈʌn juː kʊd fˈɪks`
- [outro] Next time: the scatterplot that could have saved the space shuttle Challenger.
  - `nˈɛkst tˈaɪm ðə skˈæɾɚplˌɑːt ðæt kˌʊdɐv sˈeɪvd ðə spˈeɪs ʃˈʌɾəl tʃˈælɪndʒɚ`
- [outro] Sources and the data for this episode are in the description.
  - `sˈoːɹsᵻz ænd ðə dˈeɪɾə fɔːɹ ðɪs ˈɛpɪsˌoʊd ɑːɹ ɪnðə dᵻskɹˈɪpʃən`

</details>

Spectrogram: `/home/user/Claude-code-YouTube-/reports/ep-001/long/spectrogram.png` (+ `_wave.png`)

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

Notes: sources_verified stays false until each factual claim is cross-checked against at least one cited source in sources.md (see reports/pilot/ep-001.md).

Frame samples: `/home/user/Claude-code-YouTube-/reports/ep-001/long/frames` — reviewed_by_claude=False
