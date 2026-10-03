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

## Koşu 2 — 2026-10-03 20:57 UTC (tohumlu TTS) — **REPRODUCIBLE: false** (aynı 14 cümle, aynı 200 ms)
Tohumlama işe yaradı (aynı ortamda ardışık süreçler birebir aynı) ama ana repo ile temiz klon yine farklıydı; her ikisi kendi içinde deterministik.
İzolasyon: fark **venv'i** izliyor, yolu değil; paketler ve ikili dosyalar (sha256) aynı. Fonem çıktısı farklı: "four" → `fˈɔːɹ` (ana) / `fˈoːɹ` (klon).
**Kök neden 2:** iki espeak-ng aynı süreçte karışıyor — `espeakng-loader` wheel'i kendi `libespeak-ng.so` (1.52) + verisini taşır, sistemde 1.51 var. espeak-ng veri yolunu ~160 baytlık sabit tampona yazar; klonun uzun yolu (`/tmp/claude-0/-home-user-…/scratchpad/repro2/clone/.venv/…`, ~170 karakter) sessizce yok sayılıp kütüphane derlenmiş yola düşüyor, ardından sistem sözlüğüyle fonemleştirme yapılıyor → farklı fonem → farklı ses.
**Düzeltme (commit "Pin bundled espeak-ng"):** `ytf` import edilirken `PHONEMIZER_ESPEAK_LIBRARY`/`ESPEAK_DATA_PATH` wheel'deki espeak'e sabitlenir; veri yolu 120 karakteri aşarsa `/tmp/ytf-espeak-ng-data`'ya kopyalanır (`YTF_ESPEAK_DATA_DIR` ile değiştirilebilir); Kokoro'ya `EspeakConfig` ile aynı yollar verilir; QC fonem listesi de aynı espeak'i kullanır. Doğrulama: aynı cümle iki venv'de aynı sha (`dc5e25d131c5`), süre 11.0108 s.

## Koşu 3 — sabitlenmiş espeak + tohumlu TTS, kısa yollu temiz klon (`reports/pilot/chain3.log`)
_bekleniyor_
