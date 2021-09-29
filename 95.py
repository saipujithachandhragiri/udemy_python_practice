# Take input with seperated by ',' and write them line by line in a file.

ui = list(input().split(','))
print(ui)

with open('user_inputs.txt','a+') as file:
	for i in ui:
		file.write(i+'\n')