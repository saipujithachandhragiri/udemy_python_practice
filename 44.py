# Create a script that generates a file where all letters of the English alphabet are listed three in each line. The inside of the text file would look like:
# abc
# def
# ghi
# and so on.

import string
with open("letter3.txt","w") as file:
	for i,j,k in zip(string.ascii_lowercase[0::3],string.ascii_lowercase[1::3],string.ascii_lowercase[2::3]):
		file.write(i+j+k+'\n')