x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(x)]
l2 = []
for i in range(3):
    l3 = []
    for j in range(x):
        l3.append(l[j][i])
    l2.append(l3)

# print(x, y)
# print(l)

for i in range(len(l2)):
    l2[i].sort()

# print(l2)

for i in range(x):
    count = 0
    for j in range(3):
        x = l2[j][y-1]
        if l[i][j] <= x:
            count += 1
    print(count)