import re

s = input()
x = re.search(r"\w{3}-\d{3,4}", s)
print(x.start())