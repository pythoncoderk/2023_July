import re

n = input()
x = re.sub("[a]|[e]|[i]|[o]|[u]", "", n)
print(x)