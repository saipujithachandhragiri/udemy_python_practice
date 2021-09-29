# Please download the attached ZIP file. Inside the ZIP file, there's a directory named subdirs. That directory contains other directories inside. Please write a script that counts the number of .py files contained inside subdirs and all its sub-directories.
# Expected output: 
# 3


import glob

flie_list = glob.glob('subdirs/**/*.py', recursive=True)
print(len(flie_list))