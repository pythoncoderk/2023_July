import re

s = input()
x = re.search(r"To be continued\.{3,}", s)
print(x.start())