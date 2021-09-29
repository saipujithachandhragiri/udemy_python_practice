# Create a script that generates a text file with all letters of the English alphabet inside it, one letter per line.

import string

with open('letter.txt','w') as f:
	for l in string.ascii_lowercase:
		f.write(l+'\n')