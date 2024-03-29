import math

m, n = map(int, input().split())

l = [int(input()) for i in range(m)]

l2 = [list(map(int, input().split())) for i in range(n)]

# print(m, n)
# print(l)
# print(l2)

l3 = []
for i in range(n):
    total = 0
    for j in range(m):
        x = math.floor(l[j] * (l2[i][j]/100))
        total += x
    l3.append(total)

for i in range(len(l3)):
    print(l3[i])
