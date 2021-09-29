# Count the number of "a" characters in this text file: http://www.pythonhow.com/data/universe.txt
# Expected output: 
# 47

import requests
import string

x = requests.get('http://www.pythonhow.com/data/universe.txt',headers = {'user-agent': 'customUserAgent'})
y = x.text.count('a')
print(y)