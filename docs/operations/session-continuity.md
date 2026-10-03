# Oturum kapandığında ne çalışır, ne çalışmaz

| Bileşen | Claude oturumu gerekir mi? | Nerede çalışır |
|---|---|---|
| Araştırma, senaryo yazımı, sahne planı, kaynak doğrulama, içerik kapısı (A) | **Evet** — yaratıcı/yargısal iş | Claude Code oturumu |
| TTS, render, mux, teknik QC (B), ASR round-trip, paketleme | Hayır | GitHub Actions (release-request push) veya VPS cron |
| Release/teslim | Hayır | Actions (aynı koşu) |
| Yükleme | İnsan (kanal sahibi) | YouTube Studio |
| Ölçüm notları | İnsan (isteğe bağlı) / ileride VPS kamuya açık sayfa okuma | reports/progress |

Kural: GitHub cron veya VPS zamanlayıcısı Claude'u süresiz ve ücretsiz çalıştırmaz; yeni bölüm için senaryo üretimi her zaman yeni bir Claude oturumu ister. Bu nedenle tamamlanmış senaryo tamponu (`content/queue.yaml` → `scripted`) tutulur; zamanlayıcı yalnızca `scripted` bölümleri render eder.
