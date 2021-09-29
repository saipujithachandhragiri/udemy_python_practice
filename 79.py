# Create a program that asks the user to enter a new password and check that the submitted password should contain at least one number, one uppercase letter, and at least 5 characters. If the conditions are generated, print out "Password is fine"; otherwise, keep prompting the user for a password.

while True:
	pswd = input('Enter the password:')
	if any(i.isdigit() for i in pswd) and any(i.isupper() for i in pswd) and len(pswd) >= 5:
		print('Password is fine')
		break
	else:
		print('Check password and enter again:')