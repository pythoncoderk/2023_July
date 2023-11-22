from decimal import Decimal, ROUND_HALF_UP
n, m, k = map(int, input().split())
l = list(map(float, input().split()))
l2 = [list(map(int, input().split())) for i in range(m)]
l4 = []
for i in range(m):
    l3 = []
    for j in range(n):
        l3.append(l[j] * l2[i][j])
    l3sum = sum(l3)
    l3sum2 = Decimal(str(l3sum)).quantize(Decimal("1."), rounding=ROUND_HALF_UP)
    l4.append(int(l3sum2))
l4.sort(reverse=True)
for i in range(k):
    print(l4[i])