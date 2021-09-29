#add a new employee to the json file

import json

with open('json_file.json','r+') as file:
	d = json.loads(file.read())
	d['employees'].append(dict(firstName ='Bharath',lastName ='Kandula'))
	file.seek(0)
	json.dump(d,file,indent=4,sort_keys=True)
	file.truncate()
