# Create a function that takes any string as input and returns the number of words for that string.

def wordcount(str):
	str = str.split()
	return(len(str))

str = 'bharath reddy kandula'
print(wordcount(str))	