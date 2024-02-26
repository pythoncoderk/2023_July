import re

s = input()
x = re.search(r"paiza", s)
print(x.start())