# secureflow-devsecops-pipeline 
# SecureFlow: CI/CD Süreçlerinde Otomatik Zafiyet Araması ve DevSecOps Boru Hattı

Bu proje, modern yazılım geliştirme yaşam döngüsünde (SDLC) güvenlik açıklarını erken aşamada tespit etmek amacıyla geliştirilmiş tam otomatik bir **DevSecOps CI/CD** boru hattıdır (Pipeline). "Shift-Left Security" (Güvenliği Sola Kaydırma) prensibi benimsenerek inşa edilmiştir.

---

## 🚀 Projenin Amacı ve Kapsamı
Geleneksel yazılım geliştirme süreçlerinde güvenlik testleri genellikle geliştirme döngüsünün en sonunda (Production öncesi) yapılır. Bu durum zafiyetlerin maliyetini ve çözüm süresini artırır. **SecureFlow**, kod yazım aşamasından konteyner dağıtımına kadar her adımda otomatik güvenlik denetimleri gerçekleştirerek bu açığı kapatır.

---

## 🛠️ Kullanılan Teknoloji ve Araçlar (Toolchain)

| Kategori | Araç / Teknoloji | Açıklama |
| :--- | :--- | :--- |
| **CI/CD Otomasyonu** | GitHub Actions | Sürekli entegrasyon ve güvenlik iş akışlarının yönetimi |
| **Statik Kod Analizi (SAST)** | Bandit | Python kaynak kodundaki güvenlik açıklarının tespiti |
| **Kod Standartları** | Black & Flake8 | Python kod formatı ve stil denetimi |
| **Bağımlılık Taraması (SCA)** | Pip-Audit | Proje bağımlılıklarındaki (Third-party packages) bilinen CVE zafiyetlerinin tespiti |
| **Sır / Şifre Taraması** | Gitleaks | Kod içine yanlışlıkla sızdırılmış şifre ve API anahtarlarının tespiti |
| **Konteyner Güvenliği** | Docker & Trivy | Uygulama imajının derlenmesi ve işletim sistemi/kütüphane açıklarının tespiti |
| **Kalite ve Metrik** | SonarCloud | Statik kod kalitesi ve kod kokusu (code smell) analizi |

---

## 📂 Proje Mimarisi ve Dizin Yapısı

```text
secureflow-devsecops-pipeline/
│
├── .github/
│   └── workflows/
│       ├── ci.yml              # Ana CI / Test / SonarCloud Pipeline
│       └── security.yml        # Güvenlik Tarama Pipeline (Gitleaks, Bandit, Pip-Audit, Trivy)
│
├── app/
│   ├── __init__.py
│   ├── database.py             # Güvenli veritabanı bağlantı yönetimi (Environment variables)
│   └── main.py                 # FastAPI / Flask ana uygulama katmanı
│
├── benchmark_dataset/          # Akademik test ve kıyaslama (CWE zafiyetleri)
│   ├── cwe_89_sqli.py
│   ├── cwe_78_cmd_injection.py
│   └── cwe_327_broken_crypto.py
│
├── docs/
│   └── cicd-log.md             # Süreç ve zafiyet tespit günlükleri
│
├── tests/
│   └── test_app.py             # Pytest birim testleri
│
├── Dockerfile                  # Konteyner yapılandırması
├── requirements.txt            # Proje bağımlılıkları
└── README.md                   # Proje Dokümantasyonu


---

## 🚀 Projenin Amacı ve Kapsamı
Geleneksel yazılım geliştirme süreçlerinde güvenlik testleri genellikle geliştirme döngüsünün en sonunda (Production öncesi) yapılır. Bu durum zafiyetlerin maliyetini ve çözüm süresini artırır. **SecureFlow**, kod yazım aşamasından konteyner dağıtımına kadar her adımda otomatik güvenlik denetimleri gerçekleştirerek bu açığı kapatır.

---

## ⚙️ CI/CD Süreç Akışı ve İşleyiş Mekanizması

Projemizde tetiklenen süreçler, kodun geliştirici bilgisayarından GitHub deposuna gönderilmesiyle (`git push`) başlar ve sırasıyla şu katmanlardan geçer:

```text
[ Developer (Git Push) ] 
       │
       ├──► 1. CI Pipeline (build-and-test)
       │     ├── Black & Flake8 (Kod Format ve Standart Kontrolü)
       │     ├── Pytest (Birim Testleri / Unit Tests)
       │     └── SonarCloud (Statik Kod Kalitesi ve Code Smell Analizi)
       │
       └──► 2. Security Pipeline (security-scans)
             ├── Gitleaks (Sır / Şifre Sızıntısı Taraması)
             ├── Bandit (Statik Uygulama Güvenliği - SAST)
             ├── Pip-Audit (Bağımlılık Güvenlik Taraması - SCA / CVE)
             └── Docker & Trivy (Konteyner İmajı ve İşletim Sistemi Zafiyet Taraması)