# Create a program that generates a password of 6 random alphanumeric characters.

import random
char = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = ''.join(random.sample(char,6))
print(password)