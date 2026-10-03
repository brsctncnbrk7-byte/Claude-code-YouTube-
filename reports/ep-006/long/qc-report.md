# QC report — ep-006 (long)

**Status:** `QC_PASS`  •  technical_ok=True  •  gate_ok=True

## B. Technical checks
| check | ok | detail |
|---|---|---|
| container | ✅ | {"codec": "h264", "pix_fmt": "yuv420p", "w": 1920, "h": 1080, "fps": "30/1", "audio": "aac 48000Hz", "duration": 160.467, "frames": 4814, "expected_frames": 4814} |
| blackdetect | ✅ | {} |
| silencedetect | ✅ | {} |
| loudness | ✅ | {"integrated_lufs": -14.01, "true_peak_dbtp": -2.88, "lra": 2.8} |
| subtitles | ✅ | {"cues": 46, "long_or_tall": 0} |
| text_overflow | ✅ | {} |
| frame_samples | ✅ | {"count": 18, "dir": "/home/user/Claude-code-YouTube-/reports/ep-006/long/frames", "reviewed_by_claude": true} |
| frame_content | ✅ | {"blank_frames": []} |

## C. Audio evaluation (not a human listening test)
> Audio was evaluated by phoneme review, ASR round-trip and spectrogram inspection; no human listening test was performed.

ASR: whisper-base.en int8 (sherpa-onnx) — mean WER **0.0261**, flagged (WER>0.05): 5

- [hook] WER 0.222: ref=`Two million four hundred thousand ballots, returned by mail.` hyp=`2,400,000 ballots returned by mail.`
- [hook] WER 0.231: ref=`Its prediction: Alf Landon would beat Franklin Roosevelt, fifty-seven to forty-three.` hyp=`Its prediction, Alflanden would beat Franklin Roosevelt 57-43.`
- [title] WER 0.182: ref=`Three weeks later Roosevelt won forty-six of forty-eight states.` hyp=`Three weeks later, Roosevelt, 146 of 48 states.`
- [compare_polls] WER 0.182: ref=`The Digest, with two point four million ballots: Landon fifty-seven.` hyp=`The digest with 2.4 million ballots, landed in 57.`
- [nonresponse] WER 0.071: ref=`In 1988 the political scientist Peverill Squire re-analysed that survey and concluded that both biases were real, and that the failure to respond was the larger one.` hyp=`In 1988, the political scientist Pevreel Squire re-analyzed that survey and concluded that both biases were real and that the failure to respond was the larger one.`

<details><summary>Phoneme review (IPA per sentence)</summary>

- [hook] In October 1936, an American magazine announced the result of the largest opinion poll ever taken.
  - `ɪn ɑːktˈoʊbɚ nˈaɪntiːnhˈʌndɹɪd θˈɜːɾi sˈɪks ɐn ɐmˈɛɹɪkən mˌæɡɐzˈiːn ɐnˈaʊnst ðə ɹɪzˈʌlt ʌvðə lˈɑːɹdʒɪst əpˈɪniən pˈoʊl ˈɛvɚ tˈeɪkən`
- [hook] Two million four hundred thousand ballots, returned by mail.
  - `tˈuː mˈɪliən fˈɔːɹ hˈʌndɹɪd θˈaʊzənd bˈæləts ɹᵻtˈɜːnd baɪ mˈeɪl`
- [hook] Its prediction: Alf Landon would beat Franklin Roosevelt, fifty-seven to forty-three.
  - `ɪts pɹɪdˈɪkʃən ˈælf lˈændən wʊd bˈiːt fɹˈæŋklɪn ɹˈoʊzəvˌɛlt fˈɪftisˈɛvən tə fˈɔːɹɾiθɹˈiː`
- [title] Three weeks later Roosevelt won forty-six of forty-eight states.
  - `θɹˈiː wˈiːks lˈeɪɾɚ ɹˈoʊzəvˌɛlt wˈʌn fˈɔːɹɾisˈɪks ʌv fˈɔːɹɾiˈeɪt stˈeɪts`
- [title] This is the story of how the biggest poll in history got it backwards, and why a much smaller one got it right.
  - `ðɪs ɪz ðə stˈɔːɹi ʌv hˌaʊ ðə bˈɪɡɪst pˈoʊl ɪn hˈɪstɚɹi ɡɑːt ɪt bˈækwɚdz ænd wˌaɪ ɐ mˈʌtʃ smˈɔːlɚ wˈʌn ɡɑːt ɪt ɹˈaɪt`
- [funnel] The Literary Digest had called every presidential election since 1916.
  - `ðə lˈɪɾɚɹˌɛɹi daɪdʒˈɛst hæd kˈɔːld ˈɛvɹi pɹˌɛzɪdˈɛnʃəl ᵻlˈɛkʃən sˈɪns nˈaɪntiːnhˈʌndɹɪd sˈɪkstiːn`
- [funnel] Its method was scale.
  - `ɪts mˈɛθəd wʌz skˈeɪl`
- [funnel] It mailed ten million ballots, to names taken from telephone directories, automobile registrations and its own subscriber lists.
  - `ɪt mˈeɪld tˈɛn mˈɪliən bˈæləts tə nˈeɪmz tˈeɪkən fɹʌm tˈɛlᵻfˌoʊn dᵻɹˈɛktɚɹiz ˈɔːɾəməbˌiəl ɹˌɛdʒɪstɹˈeɪʃənz ænd ɪts ˈoʊn səbskɹˈaɪbɚ lˈɪsts`
- [funnel] About twenty-four percent came back.
  - `ɐbˌaʊt twˈɛntifˈɔːɹ pɚsˈɛnt kˈeɪm bˈæk`
- [funnel] Two point four million is an enormous sample.
  - `tˈuː pˈɔɪnt fˈɔːɹ mˈɪliən ɪz ɐn ɪnˈɔːɹməs sˈæmpəl`
- [funnel] It was also the wrong one, twice over.
  - `ɪt wʌz ˈɔːlsoʊ ðə ɹˈɔŋ wˈʌn twˈaɪs ˈoʊvɚ`
- [compare_polls] Here are the three numbers side by side.
  - `hˈɪɹ ɑːɹ ðə θɹˈiː nˈʌmbɚz sˈaɪd baɪ sˈaɪd`
- [compare_polls] The Digest, with two point four million ballots: Landon fifty-seven.
  - `ðə dˈaɪdʒɛst wɪð tˈuː pˈɔɪnt fˈɔːɹ mˈɪliən bˈæləts lˈændən fˈɪftisˈɛvən`
- [compare_polls] George Gallup, a young pollster with roughly fifty thousand interviews, chosen to mirror the population by region, income and sex: Roosevelt fifty-six.
  - `dʒˈɔːɹdʒ ɡˈælʌp ɐ jˈʌŋ pˈɑːlstɚ wɪð ɹˈʌfli fˈɪfti θˈaʊzənd ˈɪntɚvjˌuːz tʃˈoʊzən tə mˈɪɹɚ ðə pˌɑːpjʊlˈeɪʃən baɪ ɹˈiːdʒən ˈɪŋkʌm ænd sˈɛks ɹˈoʊzəvˌɛlt fˈɪftisˈɪks`
- [compare_polls] The election: Roosevelt about sixty-two to thirty-eight.
  - `ðɪ ᵻlˈɛkʃən ɹˈoʊzəvˌɛlt ɐbˌaʊt sˈɪkstitˈuː tə θˈɜːɾiˈeɪt`
- [compare_polls] The small sample was close.
  - `ðə smˈɔːl sˈæmpəl wʌz klˈoʊs`
- [compare_polls] The huge one was off by nineteen points.
  - `ðə hjˈuːdʒ wˈʌn wʌz ˈɔf baɪ nˈaɪntiːn pˈɔɪnts`
- [selection] The first problem was who received a ballot.
  - `ðə fˈɜːst pɹˈɑːbləm wʌz hˌuː ɹᵻsˈiːvd ɐ bˈælət`
- [selection] In 1936, in the middle of the Depression, owning a telephone or a car marked you as better off than most voters, and better-off voters leaned Republican.
  - `ɪn nˈaɪntiːnhˈʌndɹɪd θˈɜːɾi sˈɪks ɪnðə mˈɪdəl ʌvðə dᵻpɹˈɛʃən ˈoʊnɪŋ ɐ tˈɛlᵻfˌoʊn ɔːɹ ɐ kˈɑːɹ mˈɑːɹkt juː æz bˈɛɾɚɹ ˈɔf ðɐn mˈoʊst vˈoʊɾɚz ænd bˈɛɾɚɹˈɔf vˈoʊɾɚz lˈiːnd ɹᵻpˈʌblɪkən`
- [selection] The list itself tilted toward Landon.
  - `ðə lˈɪst ɪtsˈɛlf tˈɪltᵻd təwˈɔːɹd lˈændən`
- [nonresponse] The second problem was who bothered to reply.
  - `ðə sˈɛkənd pɹˈɑːbləm wʌz hˌuː bˈɑːðɚd tə ɹᵻplˈaɪ`
- [nonresponse] Only one in four did.
  - `ˈoʊnli wˈʌn ɪn fˈɔːɹ dˈɪd`
- [nonresponse] In 1937 Gallup asked people whether they had received a Digest ballot and whether they had returned it.
  - `ɪn nˈaɪntiːnhˈʌndɹɪd θˈɜːɾi sˈɛvən ɡˈælʌp ˈæskt pˈiːpəl wˈɛðɚ ðeɪ hæd ɹᵻsˈiːvd ɐ dˈaɪdʒɛst bˈælət ænd wˈɛðɚ ðeɪ hæd ɹᵻtˈɜːnd ɪt`
- [nonresponse] Roosevelt supporters on the list had been less likely to send it back.
  - `ɹˈoʊzəvˌɛlt səpˈɔːɹɾɚz ɔnðə lˈɪst hɐdbɪn lˈɛs lˈaɪkli tə sˈɛnd ɪt bˈæk`
- [nonresponse] In 1988 the political scientist Peverill Squire re-analysed that survey and concluded that both biases were real, and that the failure to respond was the larger one.
  - `ɪn nˈaɪntiːnhˈʌndɹɪd ˈeɪɾi ˈeɪt ðə pəlˈɪɾɪkəl sˈaɪəntɪst pˈɛvɚɹˌɪl skwˈaɪɚ ɹˌiːˈænɐlˌaɪzd ðæt sˈɜːveɪ ænd kəŋklˈuːdᵻd ðæt bˈoʊθ bˈaɪəsᵻz wɜː ɹˈiːəl ænd ðætðə fˈeɪlɪɹ tə ɹᵻspˈɑːnd wʌzðə lˈɑːɹdʒɚ wˌʌn`
- [lesson] This is the lesson that survived.
  - `ðɪs ɪz ðə lˈɛsən ðæt sɚvˈaɪvd`
- [lesson] A biased sample does not get more accurate as it grows.
  - `ɐ bˈaɪəst sˈæmpəl dʌznˌɑːt ɡɛt mˈɔːɹ ˈækjʊɹət æz ɪt ɡɹˈoʊz`
- [lesson] It gets more confident.
  - `ɪt ɡˈɛts mˈɔːɹ kˈɑːnfɪdənt`
- [lesson] Two point four million ballots gave the Digest a precise estimate of the wrong population.
  - `tˈuː pˈɔɪnt fˈɔːɹ mˈɪliən bˈæləts ɡˈeɪv ðə dˈaɪdʒɛst ɐ pɹɪsˈaɪs ˈɛstᵻmət ʌvðə ɹˈɔŋ pˌɑːpjʊlˈeɪʃən`
- [aftermath] The Literary Digest folded within two years.
  - `ðə lˈɪɾɚɹˌɛɹi daɪdʒˈɛst fˈoʊldᵻd wɪðˌɪn tˈuː jˈɪɹz`
- [aftermath] Gallup's approach, small samples designed to look like the country, became the standard.
  - `ɡˈælʌps ɐpɹˈoʊtʃ smˈɔːl sˈæmpəlz dɪzˈaɪnd tə lˈʊk lˈaɪk ðə kˈʌntɹi bɪkˌeɪm ðə stˈændɚd`
- [aftermath] It would fail in its own way in 1948, but that is another episode.
  - `ɪt wʊd fˈeɪl ɪn ɪts ˈoʊn wˈeɪ ɪn nˈaɪntiːnhˈʌndɹɪd fˈɔːɹɾi ˈeɪt bˌʌt ðæt ɪz ɐnˈʌðɚɹ ˈɛpɪsˌoʊd`
- [outro] Sources for this episode are in the description.
  - `sˈɔːɹsᵻz fɔːɹ ðɪs ˈɛpɪsˌoʊd ɑːɹ ɪnðə dᵻskɹˈɪpʃən`
- [outro] Next time: Simpson's paradox, and the admissions data that said two opposite things at once.
  - `nˈɛkst tˈaɪm sˈɪmpsənz pˈæɹədˌɑːks ænd ðɪ ɐdmˈɪʃənz dˈeɪɾə ðæt sˈɛd tˈuː ˈɑːpəzˌɪt θˈɪŋz ɐtwˈʌns`

</details>

Spectrogram: `/home/user/Claude-code-YouTube-/reports/ep-006/long/spectrogram.png` (+ `_wave.png`)

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

Frame samples: `/home/user/Claude-code-YouTube-/reports/ep-006/long/frames` — reviewed_by_claude=True
