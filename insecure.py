import sqlite3

name = input("Enter username: ")
query = "SELECT * FROM users WHERE name = '" + name + "';"  # vulnerable to SQL Injection

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute(query)
print(cursor.fetchall())
conn.close()
