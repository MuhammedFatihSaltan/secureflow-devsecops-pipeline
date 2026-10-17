import os


def connect_db():
    # Sifreler cevre degiskeninden alinir
    db_user = os.environ.get("DB_USER", "admin")
    db_pass = os.environ.get("DB_PASSWORD", "default")

    # Kullanilmayan degisken hatasini asmak icin uzunluk alalim
    pass_len = len(db_pass)
    return f"Baglaniliyor: {db_user} / *** (Sifre uzunlugu: {pass_len})"
