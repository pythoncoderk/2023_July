import re

s = input()
x = re.search(r"[^\d]....", s)
print(x.start())