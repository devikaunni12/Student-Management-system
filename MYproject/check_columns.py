import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(Myapp_student)")
columns = cursor.fetchall()
print('Columns in Myapp_student:', columns)
conn.close()
