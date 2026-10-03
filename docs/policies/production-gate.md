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
Teknik ölçümler (dalga formu, loudness, sessizlik, dosya bütünlüğü) **telaffuz veya anlaşılabilirlik kanıtı değildir.** Gerçek sentezlenmiş ses üzerinde şu katmanlar çalıştırılır ve `reports/<ep>/<fmt>/audio-eval.md` olarak raporlanır:
1. **Anlaşılabilirlik — iki bağımsız ASR modeliyle round-trip** (Whisper base.en ve small.en, sherpa-onnx int8, MIT/Apache; her ikisi de `scripts/fetch_models.py` ile hem yerelde hem runner'da kurulur): her cümle için iki transkript, WER normalizasyonla (sayı/yıl/sıra sayısı/eş sesli/İngiliz yazımı); cümle skoru = iki modelin iyisi. Eşik: ortalama WER ≤ 0.05; tek cümle WER > 0.34 → bayrak.
2. **Algısal kalite — DNSMOS P.835** (Microsoft DNS-Challenge, CC BY 4.0; yalnızca QC'de kullanılır): her cümle için SIG/BAK/OVRL MOS tahmini (1–5). Eşik: OVRL medyanı ≥ 3.0; tek cümle OVRL < 2.6 → bayrak. (DNSMOS gerçek konuşma/gürültü üzerinde eğitilmiştir; temiz TTS tipik olarak 3.0–3.6 OVRL alır — eşikler bu projede ölçülen dağılıma göre belirlenmiş sezgisel değerlerdir.)
3. **Telaffuz incelemesi**: her cümlenin G2P (espeak) IPA çıktısı raporda; özel adlar, sayılar, yabancı sözcükler için beklenen telaffuzla karşılaştırılır; sapma varsa `[[görünen|söylenen]]` respelling ile yeniden sentez. Bayraklı cümleler iki transkript + IPA ile birlikte listelenir; kabul kararı ve gerekçesi `gate.notes`'a yazılır.
4. **Spektrogram/dalga incelemesi**: bayraklı cümleler için yakınlaştırılmış spektrogram (`spectrograms/`); kırpılma, klip, tekrar/atlama kontrolü (Claude görsel inceler).

**Durum kuralı:** `QC_PASS` yalnızca B teknik + A içerik + C katmanlarının tümü (iki ASR modelli round-trip, DNSMOS, fonem listesi) çalışmış ve `audio_ok=true` ise verilir. Katmanlardan biri çalışamadıysa veya `audio_ok=false` ise bölüm `QC_PASS_TECHNICAL_ONLY` alır ve STATUS'ta açık engel olarak kaydedilir.
**Sınır beyanı:** Bu katmanlar makine vekilleridir; insan dinlemesinin yerine geçmez. Her rapor şu cümleyi taşır: "Machine evaluation on the actual synthesized audio … No human listening test was performed." Kullanıcıya dinleme görevi devredilmez.
