import re

s = input()

x = re.sub("-{2,}","-", s)
print(x)