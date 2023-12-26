import re

x = input()
x = re.sub("\D", "", x)
print(x)