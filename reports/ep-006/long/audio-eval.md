# Audio evaluation — ep-006 (long)

> Machine evaluation on the actual synthesized audio: two-model ASR round-trip (intelligibility), DNSMOS P.835 (perceptual quality estimate), G2P phoneme listing (pronunciation review). No human listening test was performed.

**audio_ok = True**  •  sentences 34  •  models whisper-base.en int8, whisper-small.en int8

| metric | value | threshold |
|---|---|---|
| mean WER (best of models) | 0.0109 | ≤ 0.05 |
| mean WER base.en / small.en | 0.0261 / 0.0119 | — |
| DNSMOS OVRL median / min | 3.39 / 3.15 | median ≥ 3.0, min ≥ 2.6 |
| DNSMOS SIG / BAK median | 3.62 / 4.19 | — |

## Flagged sentences (0) — WER > 0.34 or OVRL < 2.6

## Minor ASR deviations (3) — 0.05 < WER ≤ 0.34 (proper nouns, homophones)
- [hook] WER 0.222: `Two million four hundred thousand ballots, returned by mail.` → base `2,400,000 ballots returned by mail.` • small `2,400,000 ballots returned by mail.`
- [hook] WER 0.077: `Its prediction: Alf Landon would beat Franklin Roosevelt, fifty-seven to forty-three.` → base `Its prediction, Alflanden would beat Franklin Roosevelt 57-43.` • small `Its prediction? Alf Landon would beat Franklin Roosevelt, 57-43.`
- [nonresponse] WER 0.071: `In 1988 the political scientist Peverill Squire re-analysed that survey and concluded that` → base `In 1988, the political scientist Pevreel Squire re-analyzed that survey and concluded that` • small `In 1988, the political scientist, Peverell Squire, reanalyzed that survey and concluded th`

## All sentences
| scene | dur | WER base | WER small | OVRL | SIG | BAK | text |
|---|---|---|---|---|---|---|---|
| hook | 7.34 | 0.0 | 0.0 | 3.52 | 3.74 | 4.22 | In October 1936, an American magazine announced the result of the larg |
| hook | 3.3 | 0.222 | 0.222 | 3.35 | 3.56 | 4.2 | Two million four hundred thousand ballots, returned by mail. |
| hook | 5.34 | 0.231 | 0.077 | 3.34 | 3.55 | 4.2 | Its prediction: Alf Landon would beat Franklin Roosevelt, fifty-seven  |
| title | 3.63 | 0.182 | 0.0 | 3.29 | 3.53 | 4.13 | Three weeks later Roosevelt won forty-six of forty-eight states. |
| title | 5.78 | 0.0 | 0.0 | 3.39 | 3.62 | 4.18 | This is the story of how the biggest poll in history got it backwards, |
| funnel | 5.32 | 0.0 | 0.0 | 3.39 | 3.61 | 4.2 | The Literary Digest had called every presidential election since 1916. |
| funnel | 1.24 | 0.0 | 0.0 | 3.29 | 3.55 | 4.07 | Its method was scale. |
| funnel | 8.0 | 0.0 | 0.0 | 3.52 | 3.72 | 4.24 | It mailed ten million ballots, to names taken from telephone directori |
| funnel | 1.79 | 0.0 | 0.0 | 3.43 | 3.65 | 4.19 | About twenty-four percent came back. |
| funnel | 2.53 | 0.0 | 0.0 | 3.49 | 3.7 | 4.19 | Two point four million is an enormous sample. |
| funnel | 2.01 | 0.0 | 0.0 | 3.5 | 3.72 | 4.18 | It was also the wrong one, twice over. |
| compare_polls | 2.07 | 0.0 | 0.0 | 3.15 | 3.49 | 3.93 | Here are the three numbers side by side. |
| compare_polls | 4.24 | 0.182 | 0.0 | 3.5 | 3.68 | 4.24 | The Digest, with two point four million ballots: Landon fifty-seven. |
| compare_polls | 9.87 | 0.0 | 0.0 | 3.54 | 3.74 | 4.24 | George Gallup, a young pollster with roughly fifty thousand interviews |
| compare_polls | 3.19 | 0.0 | 0.0 | 3.44 | 3.63 | 4.21 | The election: Roosevelt about sixty-two to thirty-eight. |
| compare_polls | 1.55 | 0.0 | 0.0 | 3.29 | 3.53 | 4.14 | The small sample was close. |
| compare_polls | 2.34 | 0.0 | 0.0 | 3.44 | 3.66 | 4.2 | The huge one was off by nineteen points. |
| selection | 2.41 | 0.0 | 0.0 | 3.33 | 3.58 | 4.15 | The first problem was who received a ballot. |
| selection | 10.24 | 0.0 | 0.0 | 3.48 | 3.69 | 4.22 | In 1936, in the middle of the Depression, owning a telephone or a car  |
| selection | 2.09 | 0.0 | 0.0 | 3.31 | 3.56 | 4.14 | The list itself tilted toward Landon. |
| nonresponse | 2.59 | 0.0 | 0.0 | 3.46 | 3.69 | 4.17 | The second problem was who bothered to reply. |
| nonresponse | 1.41 | 0.0 | 0.0 | 3.31 | 3.59 | 4.1 | Only one in four did. |
| nonresponse | 7.06 | 0.0 | 0.0 | 3.46 | 3.67 | 4.22 | In 1937 Gallup asked people whether they had received a Digest ballot  |
| nonresponse | 3.84 | 0.0 | 0.0 | 3.18 | 3.45 | 4.04 | Roosevelt supporters on the list had been less likely to send it back. |
| nonresponse | 11.39 | 0.071 | 0.107 | 3.51 | 3.71 | 4.23 | In 1988 the political scientist Peverill Squire re-analysed that surve |
| lesson | 1.7 | 0.0 | 0.0 | 3.32 | 3.6 | 4.08 | This is the lesson that survived. |
| lesson | 3.18 | 0.0 | 0.0 | 3.34 | 3.57 | 4.18 | A biased sample does not get more accurate as it grows. |
| lesson | 1.38 | 0.0 | 0.0 | 3.32 | 3.6 | 4.11 | It gets more confident. |
| lesson | 5.76 | 0.0 | 0.0 | 3.45 | 3.65 | 4.21 | Two point four million ballots gave the Digest a precise estimate of t |
| aftermath | 2.72 | 0.0 | 0.0 | 3.31 | 3.56 | 4.13 | The Literary Digest folded within two years. |
| aftermath | 4.82 | 0.0 | 0.0 | 3.48 | 3.68 | 4.21 | Gallup's approach, small samples designed to look like the country, be |
| aftermath | 4.87 | 0.0 | 0.0 | 3.3 | 3.57 | 4.06 | It would fail in its own way in 1948, but that is another episode. |
| outro | 2.49 | 0.0 | 0.0 | 3.39 | 3.61 | 4.15 | Sources for this episode are in the description. |
| outro | 5.69 | 0.0 | 0.0 | 3.49 | 3.7 | 4.22 | Next time: Simpson's paradox, and the admissions data that said two op |
