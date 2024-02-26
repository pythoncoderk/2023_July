import re

s = input()
x = re.search(r"accept|reject|pending", s)
print(x.start())