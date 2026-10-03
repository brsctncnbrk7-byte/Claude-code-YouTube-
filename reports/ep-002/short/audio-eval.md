# Audio evaluation — ep-002 (short)

> Machine evaluation on the actual synthesized audio: two-model ASR round-trip (intelligibility), DNSMOS P.835 (perceptual quality estimate), G2P phoneme listing (pronunciation review). No human listening test was performed.

**audio_ok = True**  •  sentences 6  •  models whisper-base.en int8, whisper-small.en int8

| metric | value | threshold |
|---|---|---|
| mean WER (best of models) | 0.0 | ≤ 0.05 |
| mean WER base.en / small.en | 0.0 / 0.0 | — |
| DNSMOS OVRL median / min | 3.46 / 3.16 | median ≥ 3.0, min ≥ 2.6 |
| DNSMOS SIG / BAK median | 3.67 / 4.21 | — |

## Flagged sentences (0) — WER > 0.34 or OVRL < 2.6

## Minor ASR deviations (0) — 0.05 < WER ≤ 0.34 (proper nouns, homophones)

## All sentences
| scene | dur | WER base | WER small | OVRL | SIG | BAK | text |
|---|---|---|---|---|---|---|---|
| s_hook | 3.46 | 0.0 | 0.0 | 3.44 | 3.63 | 4.19 | Seventy-three seconds after launch, Challenger broke apart. |
| s_hook | 3.14 | 0.0 | 0.0 | 3.48 | 3.68 | 4.22 | The night before, engineers tried to stop it with a chart. |
| s_compare | 3.76 | 0.0 | 0.0 | 3.44 | 3.65 | 4.21 | They plotted only the flights with O-ring damage: no clear trend. |
| s_compare | 4.71 | 0.0 | 0.0 | 3.52 | 3.72 | 4.23 | Add the sixteen flights with no damage, all of them warm, and the patt |
| s_compare | 1.72 | 0.0 | 0.0 | 3.16 | 3.45 | 3.99 | Damage lives at the cold end. |
| s_cta | 3.42 | 0.0 | 0.0 | 3.51 | 3.72 | 4.22 | The full story, and the model that predicted it, is on the channel. |
