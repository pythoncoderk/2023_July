import re

n = int(input())
l = [input() for i in range(n)]
# print(l)
l2 = []
for i in range(n):
    x = re.search(r"[\d]+", l[i])
    y = x.group()
    l2.append(y)
# print(l2)
for i in range(n):
    l2[i] = int(l2[i])
d = {}
for i in range(n):
    d[l2[i]] = l[i]
d = sorted(d.items())
for i in range(n):
    print(d[i][1])
