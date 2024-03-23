import math

m, n = map(int, input().split())
l = [int(input()) for i in range(m)]
l2 = [list(map(int, input().split())) for i in range(n)]

# print(m, n)
# print(l)
# print(l2)

for i in range(n):
    total = 0
    for j in range(m):
        total += math.floor((l2[i][j] / 100) * l[j])
    print(int(total))