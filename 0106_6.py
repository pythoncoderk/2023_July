import re

s = input()
x = re.search(r"[A-Z]-[\d][\d][a|b]", s)
print(x.start())