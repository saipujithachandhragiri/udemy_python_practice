# Create a program that asks the user to enter a new password and check that the submitted password should contain at least one number, one uppercase letter, and at least 5 characters. If the conditions are met, print out the reason why pointing to the specific condition/s that has not been satisfied.

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