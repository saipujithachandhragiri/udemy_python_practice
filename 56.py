# Store the dictionary in a json file.

import json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},{"firstName": "Anna", "lastName": "Smith"},{"firstName": "Peter", "lastName": "Jones"}],"owners":[{"firstName": "Jack", "lastName": "Petter"},{"firstName": "Jessy", "lastName": "Petter"}]}

with open('json_file.json','w') as file:
    json.dump(d,file,indent=4)