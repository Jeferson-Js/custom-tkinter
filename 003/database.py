import sqlite3

conn = sqlite3.connect('sistema.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    PASSWORD TEXT NOT NULL
)""")


print("Conexão ao banco de dados realizada com sucesso!")