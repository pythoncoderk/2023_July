import re

s = input()
x = re.sub(r"import \w+", "", s)
print(x)