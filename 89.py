# print countries area greater than 2000000sqkms from database given

import sqlite3

c = sqlite3.connect('database.db')
cur = c.cursor()
cur.execute('SELECT country FROM countries WHERE area>=2000000')
rows = cur.fetchall()
c.close()

for i in rows:
	print(i[0])