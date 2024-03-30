import re

s = input()

x = re.search(r"I|l|i", s)
if x is None:
    print(s)
else:
    print("caution")