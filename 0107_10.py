import re

s = input()
x = re.findall(r"\S+[@]\S+", s)

for i in x:
    print(i)