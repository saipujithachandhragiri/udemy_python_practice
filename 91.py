# Add countries in text file to database

import pandas
import sqlite3

ctrs = pandas.read_csv('ten_more_countries.txt')

db = sqlite3.connect('database.db')
cur = db.cursor()
for index,rows in ctrs.iterrows():
	print(rows['Country'],rows['Area'])
	cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)",(rows['Country'],rows['Area']))
db.commit()
db.close()	