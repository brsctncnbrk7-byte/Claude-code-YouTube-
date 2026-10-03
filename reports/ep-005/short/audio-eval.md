# Audio evaluation — ep-005 (short)

> Machine evaluation on the actual synthesized audio: two-model ASR round-trip (intelligibility), DNSMOS P.835 (perceptual quality estimate), G2P phoneme listing (pronunciation review). No human listening test was performed.

**audio_ok = True**  •  sentences 7  •  models whisper-base.en int8, whisper-small.en int8

| metric | value | threshold |
|---|---|---|
| mean WER (best of models) | 0.013 | ≤ 0.05 |
| mean WER base.en / small.en | 0.013 / 0.013 | — |
| DNSMOS OVRL median / min | 3.33 / 3.13 | median ≥ 3.0, min ≥ 2.6 |
| DNSMOS SIG / BAK median | 3.56 / 4.13 | — |

## Flagged sentences (0) — WER > 0.34 or OVRL < 2.6

## Minor ASR deviations (1) — 0.05 < WER ≤ 0.34 (proper nouns, homophones)
- [s_flow] WER 0.091: `In 1869 Charles Minard drew it as one band.` → base `In 1869, Charles Minar drew it as one band.` • small `In 1869, Charles Menard drew it as one band.`

## All sentences
| scene | dur | WER base | WER small | OVRL | SIG | BAK | text |
|---|---|---|---|---|---|---|---|
| s_hook | 5.82 | 0.0 | 0.0 | 3.41 | 3.66 | 4.17 | Four hundred and twenty-two thousand soldiers marched into Russia in 1 |
| s_hook | 1.64 | 0.0 | 0.0 | 3.3 | 3.55 | 4.13 | About ten thousand came back. |
| s_flow | 4.48 | 0.091 | 0.091 | 3.42 | 3.6 | 4.22 | In 1869 Charles Minard drew it as one band. |
| s_flow | 1.69 | 0.0 | 0.0 | 3.13 | 3.39 | 4.09 | The width is the number of men. |
| s_flow | 4.54 | 0.0 | 0.0 | 3.34 | 3.56 | 4.17 | Amber is the advance, white the retreat, and the strip below is the te |
| s_flow | 1.42 | 0.0 | 0.0 | 3.13 | 3.35 | 4.11 | Watch it thin to a thread. |
| s_cta | 1.95 | 0.0 | 0.0 | 3.33 | 3.59 | 4.13 | What the map leaves out is on the channel. |
