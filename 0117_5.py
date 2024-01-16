import re

s = input()
x = re.search(r"Math[1-3][A-C]", s)
print(x.start())