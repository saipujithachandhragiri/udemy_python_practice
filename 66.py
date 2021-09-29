# Create an English to Portuguese translation program.
# The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.
# d = dict(weather = "clima", earth = "terra", rain = "chuva") 
# Expected output: 
# Enter word: earth
# terra

# d = dict(weather = "clima", earth = "terra", rain = "chuva")
# x = input('Enter word:')
# for i in d.keys():
# 	if x == i:
# 		print(d[i])

# or

d = dict(weather = "clima", earth = "terra", rain = "chuva")

def trans(word):
	return d[word]

word = input('Enter word:')
print(trans(word))