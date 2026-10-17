# CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
import sqlite3

def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Zafiyet: Kullanıcıdan gelen veri doğrudan SQL sorgusuna ekleniyor (String concatenation)
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()