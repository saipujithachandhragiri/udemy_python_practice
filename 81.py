# include username for password checker

while True:
	u = input('Enter username:')
	with open('users.txt','r') as file:
		users = file.readlines()
		users = [i.strip('\n') for i in users]
	if u in users:
		print('username exist')
		continue
	else:
		print('username is fine')
		break

while True:
	note = []
	pswd = input('Enter the password:')
	if not any(i.isdigit() for i in pswd):
		note.append('Password must contain a number')
	if not any(i.isupper() for i in pswd):
		note.append('password must contain an upper case letter')
	if not len(pswd) >= 5:
		note.append('password must contain atleast 5 letters')
	if len(note) == 0:
		print('Password is fine')
		break
	else:
		print('Please check the following:')
		for i in note:
			print(i)