# Audio evaluation — ep-003 (long)

> Machine evaluation on the actual synthesized audio: two-model ASR round-trip (intelligibility), DNSMOS P.835 (perceptual quality estimate), G2P phoneme listing (pronunciation review). No human listening test was performed.

**audio_ok = True**  •  sentences 37  •  models whisper-base.en int8, whisper-small.en int8

| metric | value | threshold |
|---|---|---|
| mean WER (best of models) | 0.0068 | ≤ 0.05 |
| mean WER base.en / small.en | 0.0106 / 0.019 | — |
| DNSMOS OVRL median / min | 3.39 / 2.92 | median ≥ 3.0, min ≥ 2.6 |
| DNSMOS SIG / BAK median | 3.62 / 4.17 | — |

## Flagged sentences (0) — WER > 0.34 or OVRL < 2.6

## Minor ASR deviations (1) — 0.05 < WER ≤ 0.34 (proper nouns, homophones)
- [handle] WER 0.25: `Look at the curve.` → base `Look at the curves.` • small `Look at the curves.`

## All sentences
| scene | dur | WER base | WER small | OVRL | SIG | BAK | text |
|---|---|---|---|---|---|---|---|
| hook | 9.75 | 0.0 | 0.0 | 3.5 | 3.7 | 4.21 | On the second of September, 1854, one hundred and twenty-seven people  |
| hook | 2.46 | 0.0 | 0.0 | 3.21 | 3.51 | 4.03 | Most of them had fallen ill the day before. |
| hook | 1.67 | 0.0 | 0.0 | 3.5 | 3.69 | 4.22 | Nobody knew what cholera was. |
| title | 7.21 | 0.0 | 0.0 | 3.39 | 3.62 | 4.15 | This is the story of how a doctor found the source of an epidemic with |
| daily | 6.76 | 0.0 | 0.0 | 3.47 | 3.67 | 4.23 | John Snow was a physician who had argued, five years earlier, that cho |
| daily | 6.76 | 0.0 | 0.0 | 3.47 | 3.66 | 4.22 | When the outbreak began at the end of August he went to the General Re |
| daily | 1.1 | 0.0 | 0.0 | 3.22 | 3.49 | 4.06 | Here is his table. |
| daily | 2.44 | 0.0 | 0.167 | 3.1 | 3.35 | 4.08 | Almost nothing until August thirty-first. |
| daily | 1.89 | 0.0 | 0.0 | 2.92 | 3.24 | 3.87 | Then, in three days, hundreds. |
| daily | 3.41 | 0.0 | 0.0 | 3.42 | 3.62 | 4.21 | By the end of September the tally reached six hundred and sixteen. |
| dots616 | 1.92 | 0.0 | 0.0 | 3.29 | 3.54 | 4.1 | Six hundred and sixteen people. |
| dots616 | 4.32 | 0.0 | 0.0 | 3.35 | 3.58 | 4.16 | Snow walked the streets with a map and marked each death at the addres |
| dots616 | 4.25 | 0.0 | 0.0 | 3.49 | 3.7 | 4.21 | The marks piled up around one place: the public water pump on Broad St |
| dots616 | 4.13 | 0.0 | 0.0 | 3.47 | 3.68 | 4.19 | Streets a few minutes away, served by other pumps, were almost untouch |
| argument | 1.4 | 0.0 | 0.0 | 3.32 | 3.58 | 4.15 | The map made an argument. |
| argument | 4.6 | 0.0 | 0.0 | 3.46 | 3.68 | 4.2 | A workhouse near the pump had its own well, and few of its five hundre |
| argument | 6.77 | 0.0 | 0.0 | 3.47 | 3.69 | 4.22 | A brewery on Broad Street gave its workers beer and had its own water; |
| argument | 2.87 | 0.1 | 0.0 | 3.34 | 3.58 | 4.15 | The houses that drew water from the pump suffered worst. |
| argument | 2.22 | 0.0 | 0.0 | 3.31 | 3.56 | 4.1 | The pattern followed the water, not the air. |
| handle | 5.26 | 0.0 | 0.0 | 3.41 | 3.63 | 4.2 | On the evening of September seventh Snow presented his evidence to the |
| handle | 2.15 | 0.0 | 0.0 | 3.33 | 3.59 | 4.12 | The next day the pump handle was removed. |
| handle | 2.12 | 0.0 | 0.0 | 3.24 | 3.54 | 4.03 | Here is the part the legend leaves out. |
| handle | 0.94 | 0.25 | 0.25 | 3.59 | 3.78 | 4.2 | Look at the curve. |
| handle | 2.39 | 0.0 | 0.143 | 3.41 | 3.65 | 4.14 | New cases had peaked on September first. |
| handle | 5.06 | 0.0 | 0.0 | 3.33 | 3.56 | 4.18 | By the eighth, deaths had already fallen from one hundred and twenty-s |
| handle | 4.14 | 0.0 | 0.0 | 3.44 | 3.65 | 4.21 | The outbreak was ending on its own, partly because so many people had  |
| whitehead | 1.34 | 0.0 | 0.0 | 3.13 | 3.41 | 4.04 | So did the handle matter? |
| whitehead | 4.31 | 0.0 | 0.0 | 3.43 | 3.65 | 4.19 | It almost certainly prevented a second wave, and it mattered for anoth |
| whitehead | 3.1 | 0.0 | 0.0 | 3.58 | 3.75 | 4.24 | A local curate, Henry Whitehead, did not believe Snow. |
| whitehead | 3.89 | 0.0 | 0.143 | 3.4 | 3.63 | 4.19 | He set out to disprove him by re-interviewing the parish, house by hou |
| whitehead | 7.26 | 0.042 | 0.0 | 3.46 | 3.67 | 4.22 | Instead he found the first case: an infant whose washing water had bee |
| lesson | 1.67 | 0.0 | 0.0 | 3.35 | 3.6 | 4.13 | Snow never saw the bacterium. |
| lesson | 1.98 | 0.0 | 0.0 | 3.34 | 3.6 | 4.13 | It would be identified decades later. |
| lesson | 7.69 | 0.0 | 0.0 | 3.5 | 3.7 | 4.23 | What he had was a count over time, a map over space, and comparison gr |
| lesson | 2.03 | 0.0 | 0.0 | 3.38 | 3.62 | 4.13 | That is still how outbreaks are traced. |
| outro | 3.76 | 0.0 | 0.0 | 3.34 | 3.56 | 4.15 | Snow's table and the sources for this episode are in the description. |
| outro | 3.81 | 0.0 | 0.0 | 3.32 | 3.55 | 4.17 | Next time: the bombers that came back, and the holes that were not the |
