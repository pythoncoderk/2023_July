import math

m, n = map(int, input().split())
l1 = [int(input()) for i in range(m)]
l2 = [list(map(int, input().split())) for i in range(n)]

# print(m, n)
# print(l1)

# l_k = [l1[i] / 100 for i in range(m)]
l_m = [[l2[i][j] * 0.01 for j in range(m)] for i in range(n)]

# print(l_m)

for i in range(n):
    total = []
    for j in range(m):
        total.append(int(l1[j] * l_m[i][j]))
    print(sum(total))