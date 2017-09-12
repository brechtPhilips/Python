import sqlite3
import pandas


conn = sqlite3.connect("Files/database.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM countries WHERE area >= 2000000")
rows = cursor.fetchall()


df = pandas.DataFrame.from_records(rows,columns=["Rank","Country","Area","Population"])
df.to_csv("Files/countries_big_area.csv",index=False,)