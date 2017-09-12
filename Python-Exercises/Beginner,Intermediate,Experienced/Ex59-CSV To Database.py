import sqlite3
import pandas

data = pandas.read_csv("Files/ten-more-countries.txt")

conn = sqlite3.connect("Files/database.db")
cur = conn.cursor()
for index,row in data.iterrows():
    print(row["Country"],row["Area"])
    cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL )",(row["Country"],row["Area"]))
conn.commit()
conn.close()