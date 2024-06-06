from decimal import *

n, m, k = map(int, input().split())
l = list(map(float, input().split()))
l2 = [list(map(int, input().split())) for i in range(m)]

# print(n, m, k)
# print(l)
# print(l2)

l4 = []
for i in range(m):
    l3 = 0
    for j in range(n):
        x = l[j] * l2[i][j]
        l3 += x
    x = Decimal(str(l3))
    x = x.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    x = int(x)
    l4.append(x)

l4.sort(reverse=True)
for i in range(k):
    print(l4[i])