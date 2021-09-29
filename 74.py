# Please concatenate this file with this one to a single text file. The content of the output file should look like below.
# Expected output: 
# x,y
# 3,5
# 4,9
# 6,10
# 7,11
# 8,12
# 6,10
# 8,18
# 12,20
# 14,22
# 16,24

import pandas

data_1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = pandas.read_csv("sampletext_pandas.txt")
data = pandas.concat([data_1,data_2])
data.to_csv('sampletext2_pandas.txt',index=None)

# or

# import io
# import pandas
# import requests
 
# r = requests.get("http://www.pythonhow.com/data/sampledata.txt")
# c = r.content
# data1 = pandas.read_csv(io.StringIO(c.decode('utf-8')))
# data2 = pandas.read_csv("sampledata_x_2.txt")
# data12 = pandas.concat([data1, data2])
# data12.to_csv("sampledata12.txt", index=None)

# Explanation:
# In answer 1, we passed the file URL directly into read_csv . The read_csv  method uses the urllib  library internally to download the file. In case of errors with urllib you can use the more powerful library requests library as we did above.