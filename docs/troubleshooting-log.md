 
### Sorun #1 - flake8 E501 ve pytest ModuleNotFoundError 
- Tarih / Faz: 2026-10-16 / Faz 2 
- Belirti: flake8 satir cok uzun uyarisi ve pytest 'No module named app' hatasi. 
- Kok neden: Docstring 79 karakteri asti. pytest, kok dizini PYTHONPATH'e otomatik eklemedi. 
- Calisan cozum: Docstring kisaltildi. pytest yerine 'python -m pytest' komutu kullanildi. 

### Sorun #2 - GitHub Actions'da pytest ModuleNotFoundError
- Tarih / Faz: 2026-10-17 / Faz 4
- Belirti: GitHub Actions pipeline'ı pytest adımında 'No module named app' hatası ile kırıldı.
- Kök neden: `ci.yml` içinde pytest doğrudan çağrıldığı için PYTHONPATH kök dizini algılamadı.
- Çalışan çözüm: Komut `python -m pytest` olarak güncellendi.
- Öğrenilen ders: Yerelde test edilen komut formatları (modül çağırma mantığı) CI/CD ortamında da aynı şekilde kullanılmalıdır.