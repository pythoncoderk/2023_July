import re

n = int(input())
l = [input() for i in range(n)]

for i in range(len(l)):
    x = re.fullmatch(r"(\d{,3}\.){3}\d{,3}", l[i])
    if x is None:
        print(False)
    else:
        print(True)