import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'Myapp_%'")
tables = cursor.fetchall()
print('Tables:', tables)
conn.close()
