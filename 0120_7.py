from decimal import Decimal, ROUND_HALF_UP

n, m, k = map(int, input().split())
l = list(map(float, input().split()))
l2 = [list(map(int, input().split())) for i in range(m)]

# print(l)
# print(l2)

total = []
for i in range(m):
    x = []
    for j in range(n):
        x.append(l[j] * l2[i][j])
    total.append(Decimal(str(sum(x))).quantize(Decimal("0"), rounding=ROUND_HALF_UP))
total.sort(reverse=True)
for i in range(k):
    print(total[i])