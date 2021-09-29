# Create a script that uses the attached countries_by_area.txt  file as data source and prints out the top 5 most densely populated countries
# Expected output: 
# India
# Pakistan
# Nigeria
# China
# Indonesia

import pandas

c = pandas.read_csv('countries_by_area.txt')
c['density'] = c['population_2013']/c['area_sqkm']
c = c.sort_values(by='density',ascending=False)

for index,row in c[:5].iterrows():
	print(row['country'])

