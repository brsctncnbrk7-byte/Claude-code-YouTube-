# Yayınlama rehberi (kanal sahibi için tek sayfa)

Bu projede insan desteği yalnızca iki yerde gerekir: **kanal açma** ve **video yükleme**. Her şey hazır paket olarak gelir.

## A. Kanal açma (bir kez) — `channel/SETUP_CHECKLIST.md`
Hesap sahibinin yapması zorunlu olanlar (Claude yapamaz): Google hesabı/telefon doğrulaması, **2 Adımlı Doğrulama**, gelişmiş özellikler için kimlik/telefon doğrulaması, AdSense hesabı ve YPP başvurusu sırasında vergi/banka bilgileri ve sözleşme kabulü.

## B. Video yükleme (her bölüm, ~5 dakika)
1. Paketi indir: GitHub → Releases → `ep-001` → `ep-001.mp4`, `thumbnail_A.png`, `ep-001.en.srt`, `metadata.yaml`, `UPLOAD_CHECKLIST.md`. `manifest.json` içindeki sha256 ile dosyayı doğrulamak isteğe bağlı (`sha256sum ep-001.mp4`).
2. `UPLOAD_CHECKLIST.md` adımlarını sırayla uygula (başlık, açıklama, thumbnail, playlist, kitle, sentetik içerik, altyazı, zamanlama).
3. Yükleme bitince Claude'a yalnızca video URL'sini (veya zamanlandığını) bildir. Repo kayıtlarını (`content/publish-queue.yaml`, yayın zamanı) Claude günceller; kullanıcı repo dosyası düzenlemez. 30 gün sayacı, ilk herkese açık yayın Claude tarafından doğrulanmadan (kamuya açık video sayfası veya izinli erişim) başlatılmaz.
4. Shorts: `short/ep-001-short.mp4` aynı şekilde yüklenir; dikey ve ≤60 sn olduğu için otomatik Short olur; başlık `metadata-short.yaml`'dan.

## C. Zamanlama
Varsayılan yayın saati 15:00 UTC (Studio'da "Schedule"). İlk hafta: ep-001 (gün 0), ep-002 (gün 2), ep-003 (gün 4); Shorts yayından 1 gün sonra.

## D. Yapılmayacaklar
Abone/izlenme satın alma, karşılıklı abone, kendi videolarını döngüye alma, yanıltıcı başlık/thumbnail — hepsi YPP'den çıkarılma riski taşır ve bu projede yasaktır.
