import sqlite3

name = input("Enter username: ")
query = "SELECT * FROM users WHERE name = ?"

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute(query, (name,))
print(cursor.fetchall())
conn.close()
