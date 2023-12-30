import re

n = input()
m = int(input())
l = [input() for i in range(m)]
counts = 0
for i in l:
    x = re.search(n, i)
    if x is None:
        print(i)
        counts += 1

if counts == 0:
    print("ok")
