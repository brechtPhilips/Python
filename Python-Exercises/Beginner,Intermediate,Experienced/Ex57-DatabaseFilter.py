import sqlite3

#Create a connection
conn = sqlite3.connect("Files/database.db")
cursor = conn.cursor()
cursor.execute("SELECT country FROM countries WHERE area >= 2000000")
rows = cursor.fetchall()
conn.close()

for row in rows:
    print(row[0])