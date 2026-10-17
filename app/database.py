import os


def connect_db():
    # Güvenli Yöntem: Hassas veriler Çevre Değişkenlerinden (Environment Variables) okunur.
    db_user = os.environ.get("DB_USER", "admin")
    db_password = os.environ.get("DB_PASSWORD", "default_secure_pass")

    # Şifreyi loglara veya ekrana açıkça basmak (return etmek) da bir zafiyettir, bu yüzden sansürlüyoruz:
    return f"Bağlanılıyor: {db_user} / ***"
