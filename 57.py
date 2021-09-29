# Please download the file in the attachment and use Python to print out its content.

import json

with open('json_file.json','r') as file:
	d = json.loads(file.read())

print(d)

# or for ordered output use pprint

# import json
# from pprint import pprint

# with open('json_file.json','r') as file:
# 	d = json.loads(file.read())

# pprint(d)