x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(x)]

print(x, y)
print(l)

l2 = []
for i in range(3):
    l3 = []
    for j in range(x):
        l3.append(l[j][i])
    l2.append(l3)

for i in range(len(l2)):
    l2[i].sort()
print(l2)

for i in range(x):
    count = 0
    for j in range(3):
        if l2[j][0] >= l[i][j] and l2[j][1] >= l[i][j]:
            count += 1
    print(count)