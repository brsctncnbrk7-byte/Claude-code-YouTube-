# Audio evaluation — ep-003 (short)

> Machine evaluation on the actual synthesized audio: two-model ASR round-trip (intelligibility), DNSMOS P.835 (perceptual quality estimate), G2P phoneme listing (pronunciation review). No human listening test was performed.

**audio_ok = True**  •  sentences 5  •  models whisper-base.en int8, whisper-small.en int8

| metric | value | threshold |
|---|---|---|
| mean WER (best of models) | 0.01 | ≤ 0.05 |
| mean WER base.en / small.en | 0.02 / 0.01 | — |
| DNSMOS OVRL median / min | 3.45 / 3.36 | median ≥ 3.0, min ≥ 2.6 |
| DNSMOS SIG / BAK median | 3.67 / 4.19 | — |

## Flagged sentences (0) — WER > 0.34 or OVRL < 2.6

## Minor ASR deviations (0) — 0.05 < WER ≤ 0.34 (proper nouns, homophones)

## All sentences
| scene | dur | WER base | WER small | OVRL | SIG | BAK | text |
|---|---|---|---|---|---|---|---|
| s_hook | 8.25 | 0.1 | 0.05 | 3.53 | 3.72 | 4.25 | In September 1854, cholera killed one hundred and twenty-seven people  |
| s_handle | 3.9 | 0.0 | 0.0 | 3.45 | 3.68 | 4.19 | John Snow traced it to one water pump and had the handle removed. |
| s_handle | 3.24 | 0.0 | 0.0 | 3.36 | 3.58 | 4.19 | But look at his own data: the outbreak was already falling. |
| s_handle | 4.48 | 0.0 | 0.0 | 3.46 | 3.67 | 4.22 | The handle probably stopped a second wave; the map is what proved the  |
| s_cta | 2.78 | 0.0 | 0.0 | 3.4 | 3.62 | 4.19 | The full story, with Snow's table, is on the channel. |
