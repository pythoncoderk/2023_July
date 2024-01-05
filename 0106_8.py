import re

s = input()
x = re.search(r"congratulations!*", s)
print(x.start())