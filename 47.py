# Create a script that iterates through text files and checks if strings p, y, t, h, o, or n are found in the text file's content. If any of those strings is found, append that string to a list.

import glob

l = []
str = 'python'
files = glob.glob('letters/*txt')

for f in files:
	with open(f,'r') as file:
		x = file.read().strip()
	if x in str:
		l.append(x)
print(l)