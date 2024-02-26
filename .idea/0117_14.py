import re

s = input()
x = re.search(r"\$[\d]{3,5}", s)
print(x.start())