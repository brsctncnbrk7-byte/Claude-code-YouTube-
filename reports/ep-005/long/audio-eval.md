# Audio evaluation — ep-005 (long)

> Machine evaluation on the actual synthesized audio: two-model ASR round-trip (intelligibility), DNSMOS P.835 (perceptual quality estimate), G2P phoneme listing (pronunciation review). No human listening test was performed.

**audio_ok = True**  •  sentences 33  •  models whisper-base.en int8, whisper-small.en int8

| metric | value | threshold |
|---|---|---|
| mean WER (best of models) | 0.0192 | ≤ 0.05 |
| mean WER base.en / small.en | 0.0286 / 0.0377 | — |
| DNSMOS OVRL median / min | 3.39 / 2.82 | median ≥ 3.0, min ≥ 2.6 |
| DNSMOS SIG / BAK median | 3.62 / 4.16 | — |

## Flagged sentences (0) — WER > 0.34 or OVRL < 2.6

## Minor ASR deviations (5) — 0.05 < WER ≤ 0.34 (proper nouns, homophones)
- [flow_adv] WER 0.053: `Charles Joseph Minard was a civil engineer who spent his retirement drawing flows: of coal` → base `Charles Joseph Minar was a civil engineer who spent his retirement drawing flows of coal, ` • small `Charles Joseph Minar was a civil engineer who spent his retirement drawing flows of coal, `
- [flow_full] WER 0.286: `Zero degrees Réaumur on October eighteenth.` → base `0 degrees rayomer on October 18th.` • small `0° Ray Omer on Oct. 18.`
- [flow_full] WER 0.167: `Minus twenty-one on November fourteenth.` → base `-21 on November 14th.` • small `minus 21 on November 14.`
- [flow_full] WER 0.067: `Watch the band at the Berezina river, where the crossing cost thousands in two days.` → base `Watch the band at the Barry Zina River where the crossing cost thousands in two days.` • small `Watch the band at the Barysina River, where the crossing cost thousands in two days.`
- [caveat] WER 0.059: `Minard's numbers came from memoirs and dispatches, assembled decades after the war; they a` → base `Minars numbers came from memoirs and dispatches assembled decades after the war. They are ` • small `Meenar's numbers came from memoirs and dispatches, assembled decades after the war. They a`

## All sentences
| scene | dur | WER base | WER small | OVRL | SIG | BAK | text |
|---|---|---|---|---|---|---|---|
| hook | 6.94 | 0.062 | 0.0 | 3.35 | 3.61 | 4.14 | In June 1812, four hundred and twenty-two thousand soldiers crossed th |
| hook | 2.65 | 0.0 | 0.0 | 3.14 | 3.42 | 4.05 | Six months later, about ten thousand came back. |
| hook | 5.4 | 0.0 | 0.0 | 3.43 | 3.63 | 4.21 | In 1869 a retired engineer drew that fact as a single line. |
| title | 5.23 | 0.0 | 0.0 | 3.47 | 3.67 | 4.21 | This is the story of the chart many people call the best ever drawn, a |
| flow_adv | 7.3 | 0.053 | 0.053 | 3.54 | 3.71 | 4.25 | Charles Joseph Minard was a civil engineer who spent his retirement dr |
| flow_adv | 1.44 | 0.0 | 0.0 | 3.22 | 3.48 | 4.1 | Here the flow is an army. |
| flow_adv | 8.32 | 0.0 | 0.0 | 3.46 | 3.67 | 4.23 | The band starts at the Polish border, thick with three hundred and for |
| flow_adv | 2.07 | 0.0 | 0.0 | 3.4 | 3.63 | 4.16 | Smaller columns split off to the north. |
| flow_adv | 4.11 | 0.0 | 0.0 | 3.27 | 3.52 | 4.11 | Men die of heat, hunger and disease long before the first great battle |
| flow_adv | 2.79 | 0.0 | 0.0 | 3.24 | 3.49 | 4.11 | By Moscow, the band is a fraction of its width. |
| flow_full | 1.08 | 0.0 | 0.0 | 3.36 | 3.6 | 4.14 | Then the retreat. |
| flow_full | 7.05 | 0.0 | 0.0 | 3.48 | 3.7 | 4.19 | Minard drew it in a second band beneath the first, and under that a st |
| flow_full | 2.89 | 0.286 | 0.571 | 3.34 | 3.58 | 4.17 | Zero degrees Réaumur on October eighteenth. |
| flow_full | 2.37 | 0.167 | 0.167 | 3.46 | 3.67 | 4.18 | Minus twenty-one on November fourteenth. |
| flow_full | 4.63 | 0.0 | 0.077 | 3.35 | 3.6 | 4.14 | Minus thirty on December sixth, which is close to minus thirty-seven C |
| flow_full | 4.75 | 0.133 | 0.067 | 3.49 | 3.71 | 4.23 | Watch the band at the Berezina river, where the crossing cost thousand |
| flow_full | 3.34 | 0.0 | 0.0 | 3.25 | 3.47 | 4.14 | By the time the line reaches the border again, it is a thread. |
| variables | 1.99 | 0.0 | 0.0 | 3.44 | 3.66 | 4.15 | Count the things this one picture shows. |
| variables | 2.2 | 0.0 | 0.0 | 3.26 | 3.52 | 4.09 | The number of men, in the width of the band. |
| variables | 1.68 | 0.0 | 0.0 | 2.96 | 3.24 | 4.02 | Where they were, in its position. |
| variables | 1.91 | 0.0 | 0.0 | 3.41 | 3.62 | 4.2 | Which way they were going, in its colour. |
| variables | 1.07 | 0.0 | 0.25 | 3.4 | 3.63 | 4.2 | When, in the dates. |
| variables | 2.23 | 0.0 | 0.0 | 3.42 | 3.64 | 4.21 | And how cold it was, in the strip below. |
| variables | 2.85 | 0.0 | 0.0 | 3.36 | 3.6 | 4.18 | Six variables, and you can read it without a legend. |
| caveat | 1.47 | 0.0 | 0.0 | 3.23 | 3.52 | 4.0 | It also leaves things out. |
| caveat | 7.08 | 0.176 | 0.059 | 3.39 | 3.6 | 4.21 | Minard's numbers came from memoirs and dispatches, assembled decades a |
| caveat | 4.34 | 0.0 | 0.0 | 3.36 | 3.6 | 4.16 | The map shows nothing of Russian losses, or of the civilians along the |
| caveat | 3.28 | 0.0 | 0.0 | 2.82 | 3.07 | 3.92 | It is an argument about one army, made with one line. |
| why | 3.98 | 0.0 | 0.0 | 3.4 | 3.63 | 4.15 | Four hundred and twenty-two thousand to ten thousand is a statistic. |
| why | 3.8 | 0.067 | 0.0 | 3.55 | 3.76 | 4.23 | A band that thins to a thread, in the cold, is something you can feel. |
| why | 2.56 | 0.0 | 0.0 | 3.37 | 3.62 | 4.14 | That is what the chart does that the number cannot. |
| outro | 4.05 | 0.0 | 0.0 | 3.4 | 3.66 | 4.15 | Minard's figures and the sources for this episode are in the descripti |
| outro | 4.42 | 0.0 | 0.0 | 3.5 | 3.7 | 4.22 | Next time: the poll that got 1936 spectacularly wrong. |
