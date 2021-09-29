# export countries area greater than or equal to 2000000sqkm to csv file

import pandas
import sqlite3

c = sqlite3.connect('database.db')
cur = c.cursor()
cur.execute('SELECT * FROM countries WHERE area>=2000000')
rows = cur.fetchall()
c.close()

df = pandas.DataFrame.from_records(rows)
df.columns = ['Rank','Country','Area','Population']
df.to_csv('countries_big_areas.txt',index=False)