import math

m = int(input())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(m)
# print(n)
# print(l)

l2 = []
for i in l:
    l2.append(i[0])
l2 = set(l2)
l2 = list(l2)
# print(l2)
l3 = []
for i in range(len(l2)):
    x = []
    for j in range(n):
        if l2[i] == l[j][0]:
            x.append(l[j][2])
    l3.append(math.ceil(sum(x) / m))
print(sum(l3))

