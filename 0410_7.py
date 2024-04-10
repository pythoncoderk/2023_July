import re

s = input()

x = re.sub(r"[\D]", "@", s)
if "@" in x:
    print("error")
    exit()

s = int(s) * 2
print(s)