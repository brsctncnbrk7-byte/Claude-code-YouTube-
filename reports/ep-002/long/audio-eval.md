# Audio evaluation — ep-002 (long)

> Machine evaluation on the actual synthesized audio: two-model ASR round-trip (intelligibility), DNSMOS P.835 (perceptual quality estimate), G2P phoneme listing (pronunciation review). No human listening test was performed.

**audio_ok = True**  •  sentences 39  •  models whisper-base.en int8, whisper-small.en int8

| metric | value | threshold |
|---|---|---|
| mean WER (best of models) | 0.0047 | ≤ 0.05 |
| mean WER base.en / small.en | 0.0058 / 0.0047 | — |
| DNSMOS OVRL median / min | 3.41 / 2.98 | median ≥ 3.0, min ≥ 2.6 |
| DNSMOS SIG / BAK median | 3.63 / 4.19 | — |

## Flagged sentences (0) — WER > 0.34 or OVRL < 2.6

## Minor ASR deviations (1) — 0.05 < WER ≤ 0.34 (proper nouns, homophones)
- [caucus] WER 0.133: `Thiokol's management took the call offline for about thirty minutes, returned, and overrul` → base `Thio-Call's management took the call offline for about 30 minutes, returned, and overruled` • small `Thio calls management took the call offline for about 30 minutes, returned, and overruled `

## All sentences
| scene | dur | WER base | WER small | OVRL | SIG | BAK | text |
|---|---|---|---|---|---|---|---|
| hook | 7.63 | 0.0 | 0.0 | 3.55 | 3.73 | 4.25 | Seventy-three seconds after launch, on January 28, 1986, the Space Shu |
| hook | 1.32 | 0.0 | 0.0 | 3.34 | 3.57 | 4.11 | Seven people died. |
| hook | 4.11 | 0.0 | 0.0 | 3.47 | 3.68 | 4.22 | The night before, a group of engineers had tried to stop the launch wi |
| title | 5.19 | 0.0 | 0.0 | 3.51 | 3.71 | 4.23 | This is the story of the chart they drew, the chart they could have dr |
| engineers | 9.97 | 0.042 | 0.0 | 3.53 | 3.73 | 4.25 | On the evening of January 27, engineers at Morton Thiokol, the contrac |
| engineers | 3.71 | 0.0 | 0.0 | 3.35 | 3.58 | 4.16 | Their concern was the rubber O-rings that sealed the booster joints. |
| engineers | 1.44 | 0.0 | 0.0 | 3.17 | 3.45 | 4.05 | Cold makes rubber stiff. |
| engineers | 7.24 | 0.0 | 0.0 | 3.48 | 3.69 | 4.22 | Here is the kind of evidence they had: every flight on which an O-ring |
| engineers | 0.99 | 0.0 | 0.0 | 3.39 | 3.66 | 4.12 | Seven flights. |
| engineers | 3.12 | 0.0 | 0.0 | 3.38 | 3.6 | 4.18 | The coldest, at fifty-three degrees, had the most damage. |
| engineers | 3.02 | 0.0 | 0.0 | 3.24 | 3.48 | 4.14 | The rest scatter from the high fifties to seventy-five. |
| engineers | 2.67 | 0.0 | 0.0 | 3.54 | 3.75 | 4.22 | Managers looked at this and saw no clear trend. |
| compare | 1.42 | 0.0 | 0.0 | 2.98 | 3.29 | 3.96 | Now add what was left out. |
| compare | 3.22 | 0.0 | 0.0 | 3.26 | 3.52 | 4.09 | Sixteen flights had launched with no O-ring damage at all. |
| compare | 3.4 | 0.0 | 0.0 | 3.53 | 3.73 | 4.22 | Every one of them was warm: sixty-six degrees or higher. |
| compare | 2.42 | 0.0 | 0.0 | 3.43 | 3.66 | 4.18 | Put the zeros back and the picture changes. |
| compare | 1.38 | 0.0 | 0.0 | 3.1 | 3.36 | 4.08 | Damage is not random. |
| compare | 1.35 | 0.0 | 0.0 | 3.42 | 3.63 | 4.19 | It lives at the cold end. |
| all23 | 8.14 | 0.0 | 0.0 | 3.37 | 3.59 | 4.19 | Statisticians later fitted a simple model to these twenty-three flight |
| all23 | 5.05 | 0.0 | 0.0 | 3.56 | 3.77 | 4.23 | Fit the same model to the public table, and the curve climbs steeply b |
| all23 | 5.83 | 0.0 | 0.0 | 3.28 | 3.52 | 4.16 | At fifty-three degrees, the coldest launch so far, it expects about th |
| all23 | 4.93 | 0.0 | 0.0 | 3.45 | 3.65 | 4.2 | At the thirty-six degrees recorded on the pad that morning, it expects |
| all23 | 4.75 | 0.0 | 0.0 | 3.41 | 3.64 | 4.19 | The engineers' recommendation that night was to not launch below fifty |
| caucus | 2.82 | 0.0 | 0.0 | 3.36 | 3.6 | 4.15 | NASA managers pushed back on the recommendation. |
| caucus | 7.14 | 0.133 | 0.133 | 3.48 | 3.68 | 4.21 | Thiokol's management took the call offline for about thirty minutes, r |
| caucus | 1.17 | 0.0 | 0.0 | 3.2 | 3.45 | 4.12 | The launch went ahead. |
| caucus | 9.9 | 0.0 | 0.0 | 3.45 | 3.65 | 4.22 | The Presidential Commission later traced the failure to the O-ring sea |
| selection | 1.29 | 0.0 | 0.0 | 3.31 | 3.56 | 4.13 | The mistake has a name. |
| selection | 5.11 | 0.0 | 0.0 | 3.42 | 3.64 | 4.21 | The engineers selected on the outcome: they plotted only the flights w |
| selection | 2.1 | 0.0 | 0.0 | 3.16 | 3.44 | 4.03 | That throws away the comparison group. |
| selection | 4.71 | 0.0 | 0.0 | 3.22 | 3.47 | 4.11 | Without the flights that went fine, there is nothing for the damaged f |
| tufte | 7.26 | 0.0 | 0.0 | 3.47 | 3.66 | 4.23 | In 1989, three statisticians published a risk analysis using only the  |
| tufte | 4.68 | 0.0 | 0.0 | 3.42 | 3.62 | 4.2 | Their conclusion was that the probability of failure near freezing was |
| tufte | 7.07 | 0.05 | 0.05 | 3.45 | 3.66 | 4.21 | Edward Tufte later made the same point about the charts themselves: th |
| why | 1.87 | 0.0 | 0.0 | 3.39 | 3.63 | 4.15 | Twenty-three rows and two columns. |
| why | 1.84 | 0.0 | 0.0 | 3.39 | 3.6 | 4.16 | Shown in full, they told the truth. |
| why | 1.95 | 0.0 | 0.0 | 3.37 | 3.61 | 4.15 | Shown in part, they said nothing at all. |
| outro | 3.82 | 0.0 | 0.0 | 3.45 | 3.67 | 4.21 | Sources, the data table, and the model fit are in the description. |
| outro | 4.95 | 0.0 | 0.0 | 3.48 | 3.69 | 4.22 | Next time: six hundred and sixteen dots, and the map that found the so |
