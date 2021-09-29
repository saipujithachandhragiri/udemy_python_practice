# Please download the attached countries-raw.txt file. The file contains the list of country names, but it also contains some unnecessary text among the countries. 
# Please clean the list with Python by generating a new text file that contains a flawless list of country names without any other text or brake lines in it. The new file content should look like in the expected output.
# Expected output: 
# Afghanistan
# Albania
# Algeria
# Andorra
# Angola
# soon

with open('countries_raw.txt','r') as file:
	c = file.readlines()

c = [i.strip('\n') for i in c if '\n' in i]
c = [i for i in c if len(i)!=1]
c = [i for i in c if i!='Top of Page']
c = [i for i in c if i!='']

with open('countries_clean.txt','w') as f:
	for i in c:
		f.write(i+'\n')