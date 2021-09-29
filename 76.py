# Make a script that prints out the current day and time. For example Today is Sunday, December 25, 2016 .

from datetime import datetime

print(datetime.now().strftime("today is %A,%B %d,%Y"))