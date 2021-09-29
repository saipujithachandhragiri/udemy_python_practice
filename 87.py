# add missing countries to file(countrie_missing)

with open('countries_missing.txt','r') as file:
	c = file.readlines()

checklist = ["Portugal", "Germany","Spain"]
checklist = [i+'\n' for i in checklist]

updated_list = sorted(checklist+c)

with open('countries_updated.txt','w') as file:
	for i in updated_list:
		file.write(i)