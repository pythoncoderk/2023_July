import re

s = input()
x = re.search(r"clang[-]?format", s)
print(x.start())