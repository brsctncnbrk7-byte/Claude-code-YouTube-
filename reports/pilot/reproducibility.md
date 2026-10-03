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

## Koşu 3 — 2026-10-03 21:35 UTC (sabitlenmiş espeak + tohumlu TTS; klon yolu `/tmp/claude-0/r3/c`) — **REPRODUCIBLE: true**
| Ölçüt | A (ana) | B (temiz klon) | Sonuç |
|---|---|---|---|
| Süre / kare sayısı | eşit | eşit | ✅ |
| Cümle süreleri (57) | maks. fark **0.0 ms** | | ✅ |
| SRT cue, loudness | eşit | eşit | ✅ |
| Kare piksel farkı (8 örnek) | tümü **0.0** | | ✅ |
| **MP4 sha256** | **birebir aynı** | | ✅ (zorunlu değildi; bit-düzeyi deterministiklik sağlandı) |
Temiz klon derleme: 9:49 duvar (cümle başına tohumlu oturum nedeniyle TTS ~2 dk), tepe RSS **1.34 GB** (oturum yeniden yükleme; VPS gereksinimine işlendi).

Sonuç: `git clone` → `uv sync --frozen` → modeller (sha256) → `ytf build ep-001` zinciri, MASTER_PLAN §6 toleranslarını aşarak bit-düzeyinde aynı MP4 üretiyor. Bu sonuç bu makine/işletim sistemi için ölçülmüştür; farklı CPU/ORT yapısında bit eşitliği garanti edilmez, toleranslı eşitlik beklenir (CPU-only ORT, aynı wheel'ler).

## Çapraz makine doğrulaması — GitHub Actions runner (2026-10-03 22:11 UTC)
Run 37156473882 (`ubuntu-latest`, Python 3.11.16, aynı `uv.lock`, modeller sha256, sabitlenmiş espeak, tohumlu TTS) ile üretilen `ep-001.mp4`, `ep-001-short.mp4`, `ep-002.mp4`, `ep-002-short.mp4` bu ortamdaki yerel derlemelerle **bit-düzeyinde aynı** (sha256 eşit). Yani yeniden üretilebilirlik yalnızca aynı makinede değil, farklı bir CPU/işletim sistemi görüntüsünde de sağlandı. (Bit eşitliği yine de garanti olarak değil, ölçülmüş sonuç olarak kaydedilir; toleranslı tanım MASTER_PLAN §6'da kalır.)
