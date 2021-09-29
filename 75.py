# Please plot the data of ("http://www.pythonhow.com/data/sampledata.txt") file into a graph of x and y axis.

import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data.plot(x='x',y='y')
plt.show()