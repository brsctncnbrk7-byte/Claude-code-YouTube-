# Yeniden üretilebilirlik — temiz klon testi (ep-001 uzun)

Tanım: `docs/MASTER_PLAN.md` §6 (bit-düzeyi MP4 eşitliği zorunlu değil; süre/kare/cue/cümle süresi/loudness/kare piksel toleransları).
Araç: `scripts/repro_check.py`. Yöntem: repo `git clone` → `uv sync --frozen` → modeller (aynı sha256) → `ytf build ep-001` → ana build ile karşılaştırma.

## Koşu 1 — 2026-10-03 20:23 UTC (tohumsuz TTS) — **REPRODUCIBLE: false**
| Ölçüt | A (ana) | B (temiz klon) | Tolerans | Sonuç |
|---|---|---|---|---|
| Süre | 288.067 s | 288.333 s | ±1 kare | ❌ (+0.27 s) |
| Kare sayısı | 8.642 | 8.650 | eşit | ❌ |
| Cümle süreleri (57) | — | maks. fark 200 ms | ±20 ms | ❌ (14 cümle >5 ms) |
| SRT cue sayısı | 81 | 81 | eşit | ✅ |
| Loudness | −14.02 | −14.01 | ±0.5 LU | ✅ |
| Kare piksel farkı (8 örnek) | — | 6/8 tam 0; 2 örnek 0.0001–0.004 (zaman kayması) | <1/255 | ❌ (yalnızca kayma kaynaklı) |
| MP4 sha256 | farklı | — | gerekmez | bilgi |
Temiz klon derleme: 8:39 duvar, tepe RSS 836 MB (TTS önbelleksiz 70 s).

**Kök neden:** Kokoro ONNX grafiği rastgele gürültü çekiyor; aynı metin için çalıştırmalar arası örnek değerleri ±0.13 farklı, bazı cümlelerde süre tahmini/kırpma 25–200 ms kayıyor. Tek iş parçacığı çözmedi. `onnxruntime.set_seed()` oturum oluşturulmadan önce çağrılınca aynı çağrı sırası bit-düzeyinde aynı çıktı verdi → **ADR-012**: cümle başına tohumlanmış oturum (seed = hash(metin|ses|hız|dil)); test `tests/test_text.py::test_tts_deterministic_when_models_present` (3 taze oturumda birebir aynı WAV doğrulandı).
Maliyet: cümle başına ~2.1 s (oturum yükleme dahil) vs ~1.1 s.

## Koşu 2 — tohumlu TTS (sonuç `reports/pilot/chain-seeded.log` → bu tabloya işlenecek)
_bekleniyor_
