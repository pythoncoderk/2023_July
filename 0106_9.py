import re

s = input()
x = re.search(r"ID-+[\d]", s)
print(x.start())