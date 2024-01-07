import re

s = input()
x = re.search(r"([\d]|[a-f]){64}", s)
print(x.start())
print(x.group())