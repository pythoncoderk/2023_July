import re

s = input()
x = re.match(r"^Re:", s)
if x is None:
    print("No")
else:
    print("Yes")