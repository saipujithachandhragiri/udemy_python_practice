# Create a dictionary of keys a, b, c where each key has as value a list from 1 to 10, 11 to 20, and 21 to 30, respectively. Then print out the dictionary in a nice format.

from pprint import pprint

d = {'a':list(range(1,11)),'b':list(range(11,21)),'c':list(range(21,31))}
pprint(d)

# or 

# d = {'a':list(range(1,11)),'b':list(range(11,21)),'c':list(range(21,31))}
# print(d)