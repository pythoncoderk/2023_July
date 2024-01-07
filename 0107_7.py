import re

s = input()
x = re.search(r"\\\(.*\\\)$", s)
print(x.start())