import re

s = input()
x = re.findall(r"[^ ]+@[^ ]+", s)
for i in x:
    print(i)