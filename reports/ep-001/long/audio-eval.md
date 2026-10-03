# Audio evaluation — ep-001 (long)

> Machine evaluation on the actual synthesized audio: two-model ASR round-trip (intelligibility), DNSMOS P.835 (perceptual quality estimate), G2P phoneme listing (pronunciation review). No human listening test was performed.

**audio_ok = True**  •  sentences 57  •  models whisper-base.en int8, whisper-small.en int8

| metric | value | threshold |
|---|---|---|
| mean WER (best of models) | 0.0012 | ≤ 0.05 |
| mean WER base.en / small.en | 0.0076 / 0.0012 | — |
| DNSMOS OVRL median / min | 3.41 / 3.14 | median ≥ 3.0, min ≥ 2.6 |
| DNSMOS SIG / BAK median | 3.63 / 4.19 | — |

## Flagged sentences (0) — WER > 0.34 or OVRL < 2.6

## Minor ASR deviations (0) — 0.05 < WER ≤ 0.34 (proper nouns, homophones)

## All sentences
| scene | dur | WER base | WER small | OVRL | SIG | BAK | text |
|---|---|---|---|---|---|---|---|
| hook | 10.67 | 0.0 | 0.0 | 3.41 | 3.63 | 4.19 | In January 1855, the British army besieging Sevastopol was dying at a  |
| hook | 1.01 | 0.0 | 0.0 | 3.15 | 3.38 | 4.11 | Read that again. |
| hook | 6.56 | 0.0 | 0.0 | 3.27 | 3.56 | 4.04 | At that rate, disease alone would have wiped out the entire army in un |
| title | 6.57 | 0.0 | 0.0 | 3.43 | 3.65 | 4.19 | This is the story of how one woman turned that ledger into a picture,  |
| bars_all | 7.24 | 0.0 | 0.0 | 3.41 | 3.62 | 4.21 | Here is every month of the war, from April 1854 to March 1856. |
| bars_all | 3.48 | 0.0 | 0.0 | 3.44 | 3.63 | 4.23 | Blue is death from disease: cholera, typhus, dysentery. |
| bars_all | 1.42 | 0.0 | 0.0 | 3.27 | 3.51 | 4.13 | Red is death from wounds. |
| bars_all | 1.42 | 0.0 | 0.0 | 3.31 | 3.56 | 4.11 | White is everything else. |
| bars_all | 1.27 | 0.0 | 0.0 | 3.42 | 3.65 | 4.2 | The bars are not close. |
| bars_all | 5.71 | 0.0 | 0.0 | 3.29 | 3.53 | 4.17 | Over the whole war, disease killed fourteen thousand four hundred and  |
| bars_all | 3.09 | 0.0 | 0.0 | 3.45 | 3.66 | 4.2 | Wounds killed one thousand seven hundred and fifty-eight. |
| bars_all | 4.81 | 0.0 | 0.0 | 3.42 | 3.62 | 4.21 | For every soldier killed by the enemy, eight died of something that co |
| ledger | 6.85 | 0.0 | 0.0 | 3.42 | 3.64 | 4.21 | The numbers came from army returns, compiled with William Farr, the st |
| ledger | 8.72 | 0.0 | 0.0 | 3.51 | 3.71 | 4.22 | Florence Nightingale reached the barracks hospital at Scutari in Novem |
| ledger | 8.0 | 0.0 | 0.0 | 3.45 | 3.66 | 4.22 | She sorted every death into three columns: zymotic disease, meaning ep |
| ledger | 1.58 | 0.0 | 0.0 | 3.45 | 3.66 | 4.16 | Counting came before cleaning. |
| rose_y1 | 2.92 | 0.0 | 0.0 | 3.39 | 3.63 | 4.16 | In 1858 she drew this. |
| rose_y1 | 6.15 | 0.0 | 0.0 | 3.42 | 3.65 | 4.16 | Twelve wedges, one per month, starting in April 1854 and running clock |
| rose_y1 | 4.49 | 0.0 | 0.0 | 3.41 | 3.62 | 4.18 | The area of each wedge, not its length, is proportional to the number  |
| rose_y1 | 1.7 | 0.0 | 0.0 | 3.39 | 3.59 | 4.19 | Blue is preventable disease. |
| rose_y1 | 0.98 | 0.0 | 0.0 | 3.23 | 3.46 | 4.13 | Red is wounds. |
| rose_y1 | 1.42 | 0.0 | 0.0 | 3.4 | 3.63 | 4.18 | White is other causes. |
| rose_y1 | 2.13 | 0.0 | 0.0 | 3.34 | 3.57 | 4.18 | Watch what happens as winter arrives. |
| rose_y1 | 1.14 | 0.0 | 0.0 | 3.14 | 3.41 | 4.02 | Watch January. |
| rose_y2 | 3.1 | 0.0 | 0.0 | 3.31 | 3.52 | 4.18 | Now the second year, drawn at exactly the same scale. |
| rose_y2 | 4.99 | 0.0 | 0.0 | 3.46 | 3.69 | 4.2 | In March 1855 a Sanitary Commission reached Scutari. |
| rose_y2 | 7.79 | 0.0 | 0.0 | 3.49 | 3.68 | 4.23 | It flushed the sewers, cleared the latrines, and, by one widely repeat |
| rose_y2 | 1.1 | 0.0 | 0.0 | 3.29 | 3.54 | 4.1 | The wedges shrink. |
| rose_y2 | 6.96 | 0.0 | 0.0 | 3.51 | 3.7 | 4.24 | By September 1855, for the first time, more soldiers died of wounds th |
| army_size | 1.7 | 0.0 | 0.0 | 3.46 | 3.7 | 4.19 | One more thing the table shows. |
| army_size | 1.7 | 0.0 | 0.0 | 3.17 | 3.41 | 4.12 | The army itself was changing. |
| army_size | 6.48 | 0.0 | 0.0 | 3.49 | 3.72 | 4.23 | In April 1854 there were about eight thousand five hundred British sol |
| army_size | 4.77 | 0.0 | 0.0 | 3.43 | 3.66 | 4.2 | By March 1856 there were more than forty-six thousand. |
| army_size | 11.01 | 0.0 | 0.0 | 3.4 | 3.6 | 4.21 | A death count in a small army and a death count in a large one are not |
| rates | 3.41 | 0.0 | 0.0 | 3.33 | 3.57 | 4.14 | Rates tell the same story with the army's size taken out. |
| rates | 3.8 | 0.0 | 0.0 | 3.45 | 3.67 | 4.21 | The army more than doubled during the war, so raw counts can mislead. |
| rates | 11.01 | 0.32 | 0.04 | 3.29 | 3.55 | 4.13 | Per thousand men, disease deaths fell from over one thousand a year in |
| batswing | 5.69 | 0.0 | 0.0 | 3.44 | 3.66 | 4.19 | Her first attempt, later nicknamed the bat's wing, scaled the radius o |
| batswing | 3.89 | 0.0 | 0.0 | 3.51 | 3.71 | 4.23 | That exaggerates: double the deaths looks like four times the area. |
| batswing | 5.97 | 0.0 | 0.0 | 3.39 | 3.61 | 4.22 | She redrew it so that the area of each wedge carried the number, and w |
| coxcomb | 2.1 | 0.0 | 0.0 | 3.39 | 3.6 | 4.18 | Most people call the chart a coxcomb. |
| coxcomb | 7.38 | 0.0 | 0.0 | 3.47 | 3.67 | 4.24 | According to historian Hugh Small, she used that word for the printed  |
| barracks | 1.49 | 0.0 | 0.0 | 3.22 | 3.47 | 4.1 | She did not stop at the war. |
| barracks | 5.7 | 0.0 | 0.0 | 3.4 | 3.63 | 4.17 | Back in England she compared young soldiers living in barracks with ci |
| barracks | 3.12 | 0.0 | 0.0 | 3.41 | 3.61 | 4.19 | Civilians died at about eleven per thousand a year. |
| barracks | 1.41 | 0.0 | 0.0 | 3.35 | 3.6 | 4.13 | Infantry, seventeen. |
| barracks | 1.29 | 0.0 | 0.0 | 3.27 | 3.5 | 4.14 | Artillery, nineteen. |
| barracks | 1.17 | 0.0 | 0.0 | 3.15 | 3.41 | 4.06 | Guards, twenty. |
| barracks | 6.54 | 0.0 | 0.0 | 3.44 | 3.65 | 4.21 | Healthy men, already screened by a medical exam, were dying at nearly  |
| barracks | 5.71 | 0.0 | 0.0 | 3.45 | 3.67 | 4.21 | She printed two thousand copies of the report at her own expense and s |
| impact | 12.8 | 0.029 | 0.029 | 3.45 | 3.66 | 4.2 | The diagram went into her evidence for the Royal Commission on the Hea |
| impact | 6.27 | 0.083 | 0.0 | 3.49 | 3.69 | 4.22 | Reforms followed: an army medical school, routine sanitary statistics  |
| impact | 6.47 | 0.0 | 0.0 | 3.48 | 3.68 | 4.21 | In 1858 she became the first woman elected to the Statistical Society  |
| why | 2.6 | 0.0 | 0.0 | 3.41 | 3.64 | 4.19 | The report had hundreds of pages of tables. |
| why | 5.42 | 0.0 | 0.0 | 3.49 | 3.7 | 4.2 | The chart made one argument, and made it in a shape: the biggest kille |
| outro | 4.16 | 0.0 | 0.0 | 3.41 | 3.63 | 4.2 | Next time: the scatterplot that could have saved the space shuttle Cha |
| outro | 3.33 | 0.0 | 0.0 | 3.31 | 3.55 | 4.14 | Sources and the data for this episode are in the description. |
