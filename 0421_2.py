from decimal import *

n, m, k = map(int, input().split())
c = list(map(float, input().split()))
l = [list(map(int, input().split())) for i in range(m)]

# print(n, m, k)
# print(c)
# print(l)

l2 = []
for i in range(m):
    x = 0
    for j in range(n):
        x += c[j] * l[i][j]
    x = Decimal(str(x))
    x = x.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    l2.append(int(x))
l2.sort(reverse=True)
for i in range(k):
    print(l2[i])