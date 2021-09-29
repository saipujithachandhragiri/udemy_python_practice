# Create a script that reads this file, multiplies its values by two, and saves the output in a new text file.

import pandas

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data = data*2
data.to_csv('sampletext_pandas.txt',index=None)