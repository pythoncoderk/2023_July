import re

s = input()
x = re.search(r"^[Re:]", s)
if x is not None:
    print("Yes")
else:
    print("No")