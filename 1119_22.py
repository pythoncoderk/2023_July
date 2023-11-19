import re

n = input()
x = re.search("[\d]*", n)
m = x.span()
print(n[:m[1]])