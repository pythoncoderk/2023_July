import heapq

x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(x)]

# print(x, y)
# print(l)
d = {k: 0 for k in range(x)}

for i in range(3):
    point_l = []
    for j in range(x):
        point_l.append(l[j][i])
    xxx = heapq.nsmallest(y, point_l)
    for k in range(x):
        if point_l[k] in xxx:
            d[k] += 1
# print(d)

for i in d:
    print(d[i])







