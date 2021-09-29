# Please complete the script so that it prints out the expected output.
# d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list

d = {'a':list(range(1,11)),'b':list(range(11,21)),'c':list(range(21,31))}
for key in d.keys():
	print(key,'has values:',d[key])