import re

n = int(input())
s = input()

x = re.search(r"ABC", s)
if x is None:
    print(-1)
else:
    print(x.start()+1)