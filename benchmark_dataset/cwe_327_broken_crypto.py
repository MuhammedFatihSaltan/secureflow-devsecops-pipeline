# CWE-327: Use of a Broken or Risky Cryptographic Algorithm
import hashlib

def hash_password(password):
    # Zafiyet: MD5 günümüzde kırılmış ve son derece zayıf bir algoritmadır
    md5_hash = hashlib.md5()
    md5_hash.update(password.encode('utf-8'))
    return md5_hash.hexdigest()