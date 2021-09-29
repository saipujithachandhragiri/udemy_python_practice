#  Please add a new employee to the dictionary.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},{"firstName": "Anna","lastName": "Smith"},{"firstName": "Peter", "lastName": "Jones"}],"owners":[{"firstName": "Jack", "lastName": "Petter"},{"firstName": "Jessy", "lastName": "Petter"}]}
d['employees'].append(dict(firstName='Bharath',lastName='Kandula'))
print(d)