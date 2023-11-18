n, m, k = map(int, input().split())
points = list(map(float, input().split()))
l = [list(map(int, input().split())) for i in range(m)]

l2 = []
for i in range(m):
    x = 0
    for j in range(n):
        l[i][j] = points[j] * l[i][j]

for i in range(m):
    x = sum(l[i])
    l2.append(format(x, ".0f"))

l2.sort()
xxxxxx = -1
for i in range(k):
    print(l2[xxxxxx])
    xxxxxx -= 1
