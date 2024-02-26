import re

s = input()
x = re.search(r"[A-Z]-[0-9][0-9][ab]", s)
print(x.start())