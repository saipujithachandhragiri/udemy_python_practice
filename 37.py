# Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that a comma can separate some words with no space. For example, "Hi, it's me." would need to be counted as three words.

def count(file):
	with open(file,'r') as f:
		str = f.read()
	str = str.replace(',',' ')
	str_list = str.split()
	return len(str_list)

print(count("words2.txt"))