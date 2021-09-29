# Create a script that generates a file where all letters of the English alphabet are listed two in each line. The inside of the text file would look like:
# ab
# cd
# ef
# and so on.

import string
with open("letter.txt","w") as file:
	A = string.ascii_lowercase[0::2]
	B = string.ascii_lowercase[1::2]
	for i,j in zip(A,B):
		file.write(i + j+'\n')