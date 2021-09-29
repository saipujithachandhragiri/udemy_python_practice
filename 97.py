# add 'SAVE' function to 96th program

file = open('save_input.txt','a+')

while True:
	ui = input('Enter your input:')
	if ui == 'CLOSE':
		file.close()
		break
	elif ui == 'SAVE':
		file.close()
		file = open('save_input.txt','a+')
	else:
		file.write(ui + '\n')