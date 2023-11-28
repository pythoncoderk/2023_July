from decimal import Decimal, ROUND_HALF_UP

n, m, k = map(int, input().split())
l_ci = list(map(float, input().split()))
l = [list(map(int, input().split())) for i in range(m)]
# print(n, m, k)
# print(l_ci)
# print(l)
l3 = []
for i in range(m):
    x2 = 0
    l2 = []
    for j in range(n):
        x = l_ci[j] * l[i][j]
        x2 += x
    l3.append(Decimal(str(x2)).quantize(Decimal("1."), rounding=ROUND_HALF_UP))
l3.sort(reverse=True)
# print(l3)
for i in range(k):
    print(l3[i])