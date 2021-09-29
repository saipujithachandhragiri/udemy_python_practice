# Please download the words1.txt file from the attachment and then create a Python function that takes a text file as input and returns the number of words contained in the text file.

def count(file):
	with open(file,'r') as f:
		str = f.read()
		str_list = str.split()
		return len(str_list)

print(count("words1.txt"))