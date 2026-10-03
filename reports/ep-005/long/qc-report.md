# QC report — ep-005 (long)

**Status:** `QC_PASS_TECHNICAL_ONLY`  •  technical_ok=True  •  gate_ok=False

## B. Technical checks
| check | ok | detail |
|---|---|---|
| container | ✅ | {"codec": "h264", "pix_fmt": "yuv420p", "w": 1920, "h": 1080, "fps": "30/1", "audio": "aac 48000Hz", "duration": 137.633, "frames": 4129, "expected_frames": 4129} |
| blackdetect | ✅ | {} |
| silencedetect | ✅ | {} |
| loudness | ✅ | {"integrated_lufs": -14.02, "true_peak_dbtp": -3.06, "lra": 2.4} |
| subtitles | ✅ | {"cues": 40, "long_or_tall": 0} |
| text_overflow | ✅ | {} |
| frame_samples | ✅ | {"count": 16, "dir": "/home/user/Claude-code-YouTube-/reports/ep-005/long/frames", "reviewed_by_claude": false} |
| frame_content | ✅ | {"blank_frames": []} |

## C. Audio evaluation (not a human listening test)
> Audio was evaluated by phoneme review, ASR round-trip and spectrogram inspection; no human listening test was performed.

ASR: whisper-base.en int8 (sherpa-onnx) — mean WER **0.0286**, flagged (WER>0.05): 7

- [hook] WER 0.062: ref=`In June 1812, four hundred and twenty-two thousand soldiers crossed the river Niemen into Russia.` hyp=`In June 1812, 422,000 soldiers crossed the river Nieman into Russia.`
- [flow_adv] WER 0.053: ref=`Charles Joseph Minard was a civil engineer who spent his retirement drawing flows: of coal, of wine, of people.` hyp=`Charles Joseph Minar was a civil engineer who spent his retirement drawing flows of coal, of wine, of people.`
- [flow_full] WER 0.286: ref=`Zero degrees Réaumur on October eighteenth.` hyp=`0 degrees rayomer on October 18th.`
- [flow_full] WER 0.167: ref=`Minus twenty-one on November fourteenth.` hyp=`-21 on November 14th.`
- [flow_full] WER 0.133: ref=`Watch the band at the Berezina river, where the crossing cost thousands in two days.` hyp=`Watch the band at the Barry Zina River where the crossing cost thousands in two days.`
- [caveat] WER 0.176: ref=`Minard's numbers came from memoirs and dispatches, assembled decades after the war; they are estimates, not a count.` hyp=`Minars numbers came from memoirs and dispatches assembled decades after the war. They are estimates not account.`
- [why] WER 0.067: ref=`A band that thins to a thread, in the cold, is something you can feel.` hyp=`A ban that thins to a thread in the cold is something you can feel.`

<details><summary>Phoneme review (IPA per sentence)</summary>

- [hook] In June 1812, four hundred and twenty-two thousand soldiers crossed the river Niemen into Russia.
  - `ɪn dʒˈuːn wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd twˈɛlv fˈɔːɹ hˈʌndɹɪd ænd twˈɛntitˈuː θˈaʊzənd sˈoʊldʒɚz kɹˈɔst ðə ɹˈɪvɚ nˈiːmɛn ˌɪntʊ ɹˈʌʃə`
- [hook] Six months later, about ten thousand came back.
  - `sˈɪks mˈʌnθs lˈeɪɾɚɹ ɐbˌaʊt tˈɛn θˈaʊzənd kˈeɪm bˈæk`
- [hook] In 1869 a retired engineer drew that fact as a single line.
  - `ɪn wˈʌn θˈaʊzənd ˈeɪthˈʌndɹɪd sˈɪksti nˈaɪn ɐ ɹᵻtˈaɪɚd ˌɛndʒɪnˈɪɹ dɹˈuː ðæt fˈækt æz ɐ sˈɪŋɡəl lˈaɪn`
- [title] This is the story of the chart many people call the best ever drawn, and what it leaves out.
  - `ðɪs ɪz ðə stˈɔːɹi ʌvðə tʃˈɑːɹt mˈɛni pˈiːpəl kˈɔːl ðə bˈɛst ˈɛvɚ dɹˈɔːn ænd wʌt ɪt lˈiːvz ˈaʊt`
- [flow_adv] Charles Joseph Minard was a civil engineer who spent his retirement drawing flows: of coal, of wine, of people.
  - `tʃˈɑːɹlz dʒˈoʊsəf mˈaɪnɑːɹd wʌzɐ sˈɪvəl ˌɛndʒɪnˈɪɹ hˌuː spˈɛnt hɪz ɹᵻtˈaɪɚmənt dɹˈɔːɪŋ flˈoʊz ʌv kˈoʊl ʌv wˈaɪn ʌv pˈiːpəl`
- [flow_adv] Here the flow is an army.
  - `hˈɪɹ ðə flˈoʊ ɪz ɐn ˈɑːɹmi`
- [flow_adv] The band starts at the Polish border, thick with three hundred and forty thousand men in the main column, and it thins as the army marches east.
  - `ðə bˈænd stˈɑːɹts æt ðə pˈoʊlɪʃ bˈɔːɹdɚ θˈɪk wɪð θɹˈiː hˈʌndɹɪd ænd fˈɔːɹɾi θˈaʊzənd mˈɛn ɪnðə mˈeɪn kˈɑːlʌm ænd ɪt θˈɪnz æz ðɪ ˈɑːɹmi mˈɑːɹtʃᵻz ˈiːst`
- [flow_adv] Smaller columns split off to the north.
  - `smˈɔːlɚ kˈɑːlʌmz splˈɪt ˈɔf tə ðə nˈɔːɹθ`
- [flow_adv] Men die of heat, hunger and disease long before the first great battle.
  - `mˈɛn dˈaɪ ʌv hˈiːt hˈʌŋɡɚ ænd dɪzˈiːz lˈɔŋ bᵻfˌɔːɹ ðə fˈɜːst ɡɹˈeɪt bˈæɾəl`
- [flow_adv] By Moscow, the band is a fraction of its width.
  - `baɪ mˈɑːskoʊ ðə bˈænd ɪz ɐ fɹˈækʃən ʌv ɪts wˈɪtθ`
- [flow_full] Then the retreat.
  - `ðˈɛn ðə ɹᵻtɹˈiːt`
- [flow_full] Minard drew it in a second band beneath the first, and under that a strip of temperatures as the army walked back into winter.
  - `mˈaɪnɑːɹd dɹˈuː ɪɾ ɪn ɐ sˈɛkənd bˈænd bᵻnˌiːθ ðə fˈɜːst ænd ˌʌndɚ ðˌæɾə stɹˈɪp ʌv tˈɛmpɹɪtʃɚz æz ðɪ ˈɑːɹmi wˈɔːkt bˈæk ˌɪntʊ wˈɪntɚ`
- [flow_full] Zero degrees Réaumur on October eighteenth.
  - `zˈiəɹoʊ dᵻɡɹˈiːz ɹˈeɪɔːmɚɹ ˌɔn ɑːktˈoʊbɚɹ ˈeɪtiːnθ`
- [flow_full] Minus twenty-one on November fourteenth.
  - `mˈaɪnəs twˈɛntiwˈʌn ˌɔn noʊvˈɛmbɚ fˈɔːɹtiːnθ`
- [flow_full] Minus thirty on December sixth, which is close to minus thirty-seven Celsius.
  - `mˈaɪnəs θˈɜːɾi ˌɔn dᵻsˈɛmbɚ sˈɪksθ wˌɪtʃ ɪz klˈoʊs tə mˈaɪnəs θˈɜːɾisˈɛvən sˈɛlsɪəs`
- [flow_full] Watch the band at the Berezina river, where the crossing cost thousands in two days.
  - `wˈɑːtʃ ðə bˈænd æt ðə bˈɛɹɪzˌɪnɚ ɹˈɪvɚ wˌɛɹ ðə kɹˈɔsɪŋ kˈɔst θˈaʊzəndz ɪn tˈuː dˈeɪz`
- [flow_full] By the time the line reaches the border again, it is a thread.
  - `baɪ ðə tˈaɪm ðə lˈaɪn ɹˈiːtʃᵻz ðə bˈɔːɹdɚɹ ɐɡˈɛn ɪɾ ɪz ɐ θɹˈɛd`
- [variables] Count the things this one picture shows.
  - `kˈaʊnt ðə θˈɪŋz ðˈɪswˌʌn pˈɪktʃɚ ʃˈoʊz`
- [variables] The number of men, in the width of the band.
  - `ðə nˈʌmbɚɹ ʌv mˈɛn ɪnðə wˈɪtθ ʌvðə bˈænd`
- [variables] Where they were, in its position.
  - `wˌɛɹ ðeɪ wɜːɹ ɪn ɪts pəzˈɪʃən`
- [variables] Which way they were going, in its colour.
  - `wˌɪtʃ wˈeɪ ðeɪ wɜː ɡˌoʊɪŋ ɪn ɪts kˈʌlɚ`
- [variables] When, in the dates.
  - `wˌɛn ɪnðə dˈeɪts`
- [variables] And how cold it was, in the strip below.
  - `ænd hˌaʊ kˈoʊld ɪt wʌz ɪnðə stɹˈɪp bᵻlˈoʊ`
- [variables] Six variables, and you can read it without a legend.
  - `sˈɪks vˈɛɹɪəbəlz ænd juː kæn ɹˈiːd ɪt wɪðˌaʊt ɐ lˈɛdʒənd`
- [caveat] It also leaves things out.
  - `ɪɾ ˈɔːlsoʊ lˈiːvz θˈɪŋz ˈaʊt`
- [caveat] Minard's numbers came from memoirs and dispatches, assembled decades after the war; they are estimates, not a count.
  - `mˈaɪnɑːɹdz nˈʌmbɚz kˈeɪm fɹʌm mˈɛmwɑːɹz ænd dɪspˈætʃᵻz ɐsˈɛmbəld dˈɛkeɪdz ˈæftɚ ðə wˈɔːɹ ðeɪ ɑːɹ ˈɛstᵻməts nˌɑːɾə kˈaʊnt`
- [caveat] The map shows nothing of Russian losses, or of the civilians along the road.
  - `ðə mˈæp ʃˈoʊz nˈʌθɪŋ ʌv ɹˈʌʃən lˈɔsᵻz ɔːɹ ʌvðə sɪvˈɪliənz ɐlˈɔŋ ðə ɹˈoʊd`
- [caveat] It is an argument about one army, made with one line.
  - `ɪɾ ɪz ɐn ˈɑːɹɡjuːmənt ɐbˌaʊt wˈʌn ˈɑːɹmi mˌeɪd wɪð wˈʌn lˈaɪn`
- [why] Four hundred and twenty-two thousand to ten thousand is a statistic.
  - `fˈɔːɹ hˈʌndɹɪd ænd twˈɛntitˈuː θˈaʊzənd tə tˈɛn θˈaʊzənd ɪz ɐ stɐtˈɪstɪk`
- [why] A band that thins to a thread, in the cold, is something you can feel.
  - `ɐ bˈænd ðæt θˈɪnz tʊ ɐ θɹˈɛd ɪnðə kˈoʊld ɪz sˈʌmθɪŋ juː kæn fˈiːl`
- [why] That is what the chart does that the number cannot.
  - `ðæt ɪz wʌt ðə tʃˈɑːɹt dˈʌz ðætðə nˈʌmbɚ kænˈɑːt`
- [outro] Minard's figures and the sources for this episode are in the description.
  - `mˈaɪnɑːɹdz fˈɪɡjɚz ænd ðə sˈɔːɹsᵻz fɔːɹ ðɪs ˈɛpɪsˌoʊd ɑːɹ ɪnðə dᵻskɹˈɪpʃən`
- [outro] Next time: the poll that got 1936 spectacularly wrong.
  - `nˈɛkst tˈaɪm ðə pˈoʊl ðæt ɡɑːt nˈaɪntiːnhˈʌndɹɪd θˈɜːɾi sˈɪks spɛktˈækjʊlɚli ɹˈɔŋ`

</details>

Spectrogram: `/home/user/Claude-code-YouTube-/reports/ep-005/long/spectrogram.png` (+ `_wave.png`)

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

Frame samples: `/home/user/Claude-code-YouTube-/reports/ep-005/long/frames` — reviewed_by_claude=False
