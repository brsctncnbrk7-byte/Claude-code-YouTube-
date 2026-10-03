# Üretim kapısı — her bölüm için zorunlu kontrol listesi

Bir bölüm `packaged` durumuna geçmeden önce `uv run ytf qc <ep>` raporunda aşağıdakilerin tümü görünür. Kapı, teknik ve içerik kalitesini **ayrı** raporlar.

## A. İçerik (insan yargısı — Claude oturumunda yapılır, otomatik değil)
- [ ] Tez cümlesi var; bölüm başka bir kaynağın yeniden anlatımı değil.
- [ ] Her olgusal iddia `sources.md`'de kaynaklı (URL, erişim tarihi, birincil/ikincil).
- [ ] Her sahnenin "görsel neyi açıklıyor" satırı dolu; dekoratif tekrar yok.
- [ ] Önceki bölümlerle konu/veri/görsel yapı çakışması yok (`content/queue.yaml` karşılaştırması).
- [ ] Başlık ve thumbnail içerikle örtüşüyor; yanıltıcı vaat yok.
- [ ] Reklam uygunluğu notu yazılı; hassas konu dili ölçülü.
- [ ] Lisans kaydı: fontlar, veri setleri, model, kod — `licenses.md` tam.

## B. Teknik (otomatik, `ytf qc`)
- [ ] ffprobe: h264 yuv420p 1920×1080 (veya 1080×1920 Shorts) 30 fps, AAC 48 kHz, süre = plan ± %2.
- [ ] `blackdetect` (d≥0.5 s) ve `silencedetect` (−50 dB, d≥2 s) sadece planlı yerlerde.
- [ ] Loudness: integrated ≈ −14 LUFS ± 1, true peak ≤ −1 dBTP.
- [ ] SRT/VTT: segment sayısı = cümle sayısı; her segment ses sınırlarıyla ≤ 300 ms sapma; satır ≤ 42 karakter, ≤ 2 satır.
- [ ] Metin taşması: DOM ölçümünde hiçbir metin kutusu sahne sınırını aşmıyor.
- [ ] Kare örnekleri: her sahneden ≥ 2 kare `reports/<ep>/frames/` altında; Claude bunları **görsel olarak inceledi** ve notunu yazdı.
- [ ] manifest.json: tüm teslim dosyaları sha256 ile.

## C. Ses değerlendirmesi (narrated bölümler için zorunlu; tam QC_PASS buna bağlı)
Teknik ölçümler (dalga formu, loudness, sessizlik) **telaffuz veya anlaşılabilirlik onayı değildir.** Şu üç katman birlikte raporlanır:
1. **Sentez öncesi fonem incelemesi**: her cümlenin G2P çıktısı (IPA) metin olarak kaydedilir; özel adlar, sayılar, kısaltmalar, yabancı sözcükler için beklenen telaffuz ile karşılaştırılır; sapma varsa `pronunciation.yaml` ile düzeltilip yeniden sentezlenir.
2. **Sentez sonrası ASR round-trip**: Whisper (base.en, int8) ile transkript; cümle bazında WER; WER > 0.05 olan cümleler listelenir ve nedeni (telaffuz / ASR hatası) değerlendirilir; gerekiyorsa yeniden yazım/yeniden sentez.
3. **Spektrogram/dalga incelemesi**: cümle başı-sonu kırpılma, klip, tekrar/atlama, anormal hız; görüntü olarak Claude tarafından incelenir.

**Sınır beyanı:** Bu üç katman insan dinlemesinin yerine geçmez. Rapor şu cümleyi içerir: "Audio was evaluated by phoneme review, ASR round-trip and spectrogram inspection; no human listening test was performed." Katmanlardan biri çalıştırılamadıysa bölüm `QC_PASS_TECHNICAL_ONLY` alır, `QC_PASS` almaz ve bu durum STATUS'ta açık engel olarak kaydedilir. Kullanıcıya dinleme görevi devredilmez.
