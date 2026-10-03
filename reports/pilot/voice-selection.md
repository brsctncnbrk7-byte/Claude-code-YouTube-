# Ses seçimi — Kokoro-82M (2026-10-03)

Deney (scratch, `kokoro-onnx 0.6.1`): aynı 5 cümlelik örnek metin 6 sesle sentezlendi ve Whisper base.en ile geri yazıldı.
| Ses | Süre (s) | Sentez (s) | ASR WER |
|---|---|---|---|
| af_heart | 23.6 | 7.6 | ≤ 0.016 (örnek: "cholera"→"Collara" dışında tam) |
| am_michael | 25.9 | 6.8 | ≤ 0.016 |
| bf_emma | 22.3 | 5.4 | 0.000 |
| bm_george | 24.3 | 6.4 | 0.016 |
| af_bella | 24.1 | 6.0 | 0.000 |
| am_adam | 22.3 | 5.7 | 0.016 |
Tüm sesler anlaşılabilirlik açısından eşdeğer çıktı (fark tek bir özel adda). **Karar: `af_heart`** (Amerikan İngilizcesi, nötr tını; Kokoro dağıtımındaki varsayılan/örnek ses). Derin değerlendirmede (DNSMOS) af_heart OVRL medyanı 3.3–3.4 (reports/ep-00X/*/audio-eval.md). İnsan dinlemesi yapılmadı; seçim ASR + DNSMOS vekilleriyle ve varsayılan ses olmasıyla gerekçelendirildi. Yeniden değerlendirme: 7. gün izleyici tutma verisi.
