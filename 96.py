# create a programs that asks input repeatedly until 'CLOSE' is given and append to a text file.

file = open('repeated_input.txt','a+')

while True:
	ui = input('Enter your input:')
	if ui == 'CLOSE':
		file.close()
		break
	else:
		file.write(ui+'\n')