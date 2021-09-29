# letter extractor

import glob

l = []
files = glob.glob("letters/*.txt")

for f in files:
	with open(f,'r')as file:
		l.append(file.read().strip('\n'))
print(l)