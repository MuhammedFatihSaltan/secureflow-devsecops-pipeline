# Güvenli ve hafif bir imaj olan python:3.12-slim kullanıyoruz
FROM python:3.12-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Sadece gereksinimleri kopyala ve yükle (Önbelleği verimli kullanmak için)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodlarını kopyala
COPY . .

# Güvenlik için root olmayan bir kullanıcı oluşturup ona geçiş yap (İyi Pratik)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Uygulamanın çalışacağı port
EXPOSE 5000

# Uygulamayı başlat
CMD ["python", "app/main.py"]