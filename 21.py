# Filter the dictionary by removing all items with a value of greater than 1.
# d = {"a": 1, "b": 2, "c": 3}

dic = {'a':1,'b':2,'c':3}
dic = dict((key,value) for key,value in dic.items() if value<=1)
print(dic)