import re

n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

l2 = l[::]
for i in range(n):
    l2[i] = re.sub(r"[\D]", "", l2[i])
for i in range(n):
    l2[i] = int(l2[i])

# print(l2)

l3 = []
for i in range(n):
    l4 = []
    l4.append(l[i])
    l4.append(l2[i])
    l3.append(l4)

# print(l3)

sort_l = sorted(l3, key=lambda x: x[1])
# print(sort_l)

for i in range(n):
    print(sort_l[i][0])