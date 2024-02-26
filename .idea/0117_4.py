import re

s = input()
x = re.search(r"p..za", s)
print(x.start())