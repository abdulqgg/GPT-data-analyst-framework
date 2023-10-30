import sqlite3

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

cursor.execute('SELECT COUNT(*) FROM sqlite_sequence;')

rows = cursor.fetchall()
print(rows)