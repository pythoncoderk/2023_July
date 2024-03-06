from decimal import *

n, m, k = map(int, input().split())
l = list(map(float, input().split()))
l2 = [list(map(int, input().split())) for i in range(m)]

# print(n, m, k)
# print(l)
# print(l2)

l3 = []
for i in range(m):
    total = 0
    for j in range(n):
        total += l[j] * l2[i][j]
    total_d = Decimal(str(total))
    total_d = total_d.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    l3.append(total_d)
l3.sort(reverse=True)
# print(l3)

for i in range(k):
    print(l3[i])