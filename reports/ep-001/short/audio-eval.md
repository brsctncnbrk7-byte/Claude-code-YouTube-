# Audio evaluation — ep-001 (short)

> Machine evaluation on the actual synthesized audio: two-model ASR round-trip (intelligibility), DNSMOS P.835 (perceptual quality estimate), G2P phoneme listing (pronunciation review). No human listening test was performed.

**audio_ok = True**  •  sentences 9  •  models whisper-base.en int8, whisper-small.en int8

| metric | value | threshold |
|---|---|---|
| mean WER (best of models) | 0.0 | ≤ 0.05 |
| mean WER base.en / small.en | 0.0 / 0.0556 | — |
| DNSMOS OVRL median / min | 3.29 / 3.12 | median ≥ 3.0, min ≥ 2.6 |
| DNSMOS SIG / BAK median | 3.56 / 4.13 | — |

## Flagged sentences (0) — WER > 0.34 or OVRL < 2.6

## Minor ASR deviations (0) — 0.05 < WER ≤ 0.34 (proper nouns, homophones)

## All sentences
| scene | dur | WER base | WER small | OVRL | SIG | BAK | text |
|---|---|---|---|---|---|---|---|
| s_hook | 9.02 | 0.0 | 0.0 | 3.32 | 3.53 | 4.18 | In January 1855 the British army was dying at a rate of one thousand a |
| s_hook | 1.53 | 0.0 | 0.0 | 3.29 | 3.57 | 4.08 | Almost none of it was combat. |
| s_rose | 1.73 | 0.0 | 0.5 | 3.26 | 3.56 | 4.04 | Florence Nightingale drew this. |
| s_rose | 1.21 | 0.0 | 0.0 | 3.12 | 3.41 | 3.99 | Each wedge is a month. |
| s_rose | 1.86 | 0.0 | 0.0 | 3.18 | 3.45 | 4.06 | Its area is the number of deaths. |
| s_rose | 1.7 | 0.0 | 0.0 | 3.39 | 3.59 | 4.19 | Blue is preventable disease. |
| s_rose | 0.98 | 0.0 | 0.0 | 3.23 | 3.46 | 4.13 | Red is wounds. |
| s_rose | 3.6 | 0.0 | 0.0 | 3.35 | 3.57 | 4.19 | For every soldier killed by the enemy, eight died of disease. |
| s_cta | 3.34 | 0.0 | 0.0 | 3.43 | 3.64 | 4.2 | The full story, and what the chart changed, is on the channel. |
