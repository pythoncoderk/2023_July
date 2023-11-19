import re

n = input()
x = re.search(r"[I]|[i]|[l]", n)
if x != None:
    print("caution")
else:
    print(n)