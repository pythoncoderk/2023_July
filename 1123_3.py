import re

n = input()
m = int(input())
l = [str(input()) for i in range(m)]
nons = 0
for i in range(m):
    x = re.search(n, l[i])
    if x == None:
        print(l[i])
    else:
        nons += 1
if nons == m:
    print("none")
