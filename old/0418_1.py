n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

for i in range(n):
    l[i][1] = int(l[i][1])

# print(n)
# print(l)

l2 = [l[i][0] for i in range(n)]
# print(l2)

set_l2 = set(l2)

d = {l2[k]: l2.count(l2[k]) for k in range(n)}
# print(d)

point = 0
name = ""
for i in set_l2:
    if d[i] > point:
        point = d[i]
        name = i
for i in set_l2:
    d[i] = 0

for i in range(n):
    d[l[i][0]] += l[i][1]

# print(d)

point2 = 0
name2 = ""

for i in set_l2:
    if d[i] > point2:
        point2 = d[i]
        name2 = i

print(name)
print(name2)
