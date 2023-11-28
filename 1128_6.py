from decimal import Decimal, ROUND_HALF_UP

n, m, k = map(int, input().split())
l_ci = list(map(float, input().split()))
l = [list(map(int, input().split())) for i in range(m)]
print(n, m, k)
print(l_ci)
print(l)
l2 = []
x2 = 0
for i in range(m):
    for j in range(n):
        x = l_ci[j] * l[i][j]
        x2 += x
        l2.append(Decimal(str(423.54)).quantize(Decimal("1."), rounding=ROUND_HALF_UP))
print(l2)
