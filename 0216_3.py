import re

n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

l2 = l[::]
changes = []
for i in range(n):
    x = re.sub(f"\D", "", l[i])
    changes.append(int(x))
d = {changes[k]: l[k] for k in range(n)}

d2 = sorted(d.items())
# print(list(d2))

for i in range(n):
    print(d2[i][1])