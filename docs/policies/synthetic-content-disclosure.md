# Değiştirilmiş/sentetik içerik beyanı — kayıt 2026-10-03

- Kaynak: https://support.google.com/youtube/answer/14328491 — `unverified` (bu ortamdan açılamadı). İkincil kaynaklar (`secondary`, WebSearch 2026): beyan, **gerçekçi görünen** ve gerçek sanılabilecek değiştirilmiş/sentetik içerik için zorunlu (gerçek kişinin söylemediği sözler, gerçek olayların değiştirilmesi, gerçekçi sahte sahneler). Açıkça animasyon/gerçekçi olmayan içerik, AI anlatım sesi (başkasının sesi klonlanmamışsa), senaryo yardımı, renk düzeltme beyan gerektirmez. Beyan para kazanmayı etkilemez.

## Bu kanal için karar (gerekçeli)
- İçerik: tamamen programatik animasyon/grafik + sentetik anlatıcı sesi (Kokoro-82M, gerçek bir kişiyi taklit etmez).
- Gerçek kişi görüntüsü/sesi, gerçekçi sahte olay yok → ikincil kaynaklara göre beyan zorunlu değil.
- **Uygulama:** Her yükleme paketinde `metadata.yaml → synthetic_disclosure` alanı bölüm bazında doldurulur. Varsayılan: `altered_or_synthetic: false`, gerekçe yazılı. Bölümde gerçekçi yeniden canlandırma/gerçek kişi benzeri unsur varsa `true`. Ayrıca açıklama metninde şeffaflık cümlesi: "Narration is a synthetic voice (Kokoro TTS); all visuals are generated from the cited data."
- Resmî metin okunamadığı için bu karar `unverified` kalır; ChatGPT yardım talebinde yeniden doğrulama maddesi var. Doğrulama sonucu değişirse tüm paketler güncellenir.
