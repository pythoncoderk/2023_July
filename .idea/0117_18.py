import re

s = input()
x = re.search(r"(%[\w]{2}){2,}", s)
print(x.start())