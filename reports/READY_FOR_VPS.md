# READY_FOR_VPS değerlendirmesi — TASLAK (henüz ilan edilmedi)

Durum: **HAZIR DEĞİL (son doğrulama)** — ep-003 release varlıklarının sha256 doğrulaması ve ep-001/ep-002 yeniden yayımının tamamlanması bekleniyor; ardından ilan edilecek. Bu dosya ölçütler kapandıkça kanıt bağlantılarıyla güncellenir; `READY_FOR_VPS / GITHUB PREPARATION COMPLETE` ancak 8/8 kanıtlandığında yazılır.

| # | Ölçüt (MASTER_PROMPT §10) | Durum | Kanıt |
|---|---|---|---|
| 1 | Güncel kaynaklı araştırma, niş/dil, marka, 30 gün planı | ✅ | docs/research/*, docs/policies/*, ADR-006/010/011, docs/MASTER_PLAN.md, channel/brand.md |
| 2 | Ücretsiz araçların ticari/teknik uygunluğu | ✅ (etiketli) | docs/research/tools-and-licenses.md (ayrı satırlar; REJECTED listesi) |
| 3 | Pilot uçtan uca + ikinci konu + Shorts yolu | ✅ | reports/pilot/ep-001.md, ep-002.md; dist/ep-001, dist/ep-002 (uzun+Short) QC_PASS |
| 4 | İlk hafta yayın paketleri (placeholder yok) | ✅ (release doğrulaması bekleniyor) | ep-001, ep-002, ep-003 uzun + 3 Short QC_PASS, `dist/` paketleri tam; ep-003 release koşusu sürüyor |
| 5 | Gerçek CPU/RAM/disk/render/kota ölçümü → VPS gereksinimi | ✅ | reports/pilot/render-benchmark.md, reports/quota/actions-ep-00*.md, docs/operations/vps-setup.md (denenmedi etiketli) |
| 6 | Temiz klondan tek komutla yeniden üretim; hata/devam mekanizması | ✅ | reports/pilot/reproducibility.md Koşu 3: REPRODUCIBLE true, MP4 sha256 birebir; checkpoint/retry: tests/test_jobs.py, docs/operations/recovery.md |
| 7 | Büyük çıktılar erişilebilir/ücretsiz/kalıcı teslim + manifest/checksum | ✅ | GitHub Releases `ep-001`, `ep-002` (21 varlık); sha256 doğrulandı (reports/quota/actions-ep-00*.md) |
| 8 | Kanal/yükleme paketleri, hesap sahibi zorunlulukları, analytics sınırları, ücretsiz sınırlar, VPS rehberi | ✅ | channel/SETUP_CHECKLIST.md, dist/*/UPLOAD_CHECKLIST.md, docs/operations/{publishing,measurement,github-quota,vps-setup,session-continuity}.md |
