x, y, z = map(int, input().split())
points = list(map(float, input().split()))
l = [list(map(int, input().split())) for i in range(y)]
l2 = []
for i in range(y):
    a = 0
    for j in range(x):
        a += l[i][j] * points[j]
    l2.append(a)
l3 = []
for i in l2:
    l3.append(format(i, ".0f"))
l3.sort()
xyz = -1
for i in range(z):
    print(l3[xyz])
    xyz -= 1
