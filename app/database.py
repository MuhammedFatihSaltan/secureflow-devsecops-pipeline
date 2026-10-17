# DİKKAT: Bu kod eğitim amaçlı bilinçli bir zafiyet içermektedir! (Hardcoded Secret)
def connect_db():
    db_user = "admin"
    db_password = "supersecretpassword123!" # Zafiyet: Şifre doğrudan kodun içinde!
    return f"Bağlanılıyor: {db_user} / {db_password}"