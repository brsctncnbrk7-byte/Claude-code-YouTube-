# Audio evaluation — ep-006 (short)

> Machine evaluation on the actual synthesized audio: two-model ASR round-trip (intelligibility), DNSMOS P.835 (perceptual quality estimate), G2P phoneme listing (pronunciation review). No human listening test was performed.

**audio_ok = True**  •  sentences 5  •  models whisper-base.en int8, whisper-small.en int8

| metric | value | threshold |
|---|---|---|
| mean WER (best of models) | 0.0 | ≤ 0.05 |
| mean WER base.en / small.en | 0.04 / 0.0 | — |
| DNSMOS OVRL median / min | 3.35 / 3.24 | median ≥ 3.0, min ≥ 2.6 |
| DNSMOS SIG / BAK median | 3.6 / 4.17 | — |

## Flagged sentences (0) — WER > 0.34 or OVRL < 2.6

## Minor ASR deviations (0) — 0.05 < WER ≤ 0.34 (proper nouns, homophones)

## All sentences
| scene | dur | WER base | WER small | OVRL | SIG | BAK | text |
|---|---|---|---|---|---|---|---|
| s_hook | 6.86 | 0.0 | 0.0 | 3.46 | 3.66 | 4.22 | In 1936 the biggest poll in history, two point four million ballots, p |
| s_compare | 4.29 | 0.0 | 0.0 | 3.47 | 3.68 | 4.22 | Gallup, with fifty thousand interviews chosen to mirror the country, g |
| s_compare | 3.51 | 0.2 | 0.0 | 3.34 | 3.57 | 4.16 | The Digest asked the wrong people, and the wrong people answered. |
| s_compare | 1.61 | 0.0 | 0.0 | 3.24 | 3.51 | 4.1 | Size does not fix bias. |
| s_cta | 1.77 | 0.0 | 0.0 | 3.35 | 3.6 | 4.17 | The full story is on the channel. |
