m, n = map(int, input().split())
l = [list(map(int, input().split())) for i in range(m)]

# print(m, n)
# print(l)

max_l = 0

l2 = []
l3 = []
for i in range(m - n + 1):
    total = 0
    l4 = []
    for j in range(i, i + n):
        total += l[j][1]
        l4.append(l[j][0])
    l2.append(total)
    x = l4[0]
    y = l4[-1]
    l3.append([x, y])

# print(l2)

min_l = min(l2)
z = l2.index(min_l)

print(*l3[z])
