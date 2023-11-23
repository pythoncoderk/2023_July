from decimal import Decimal, ROUND_HALF_UP

n, m = map(int, input().split())
l = [int(input()) for i in range(m)]
# print(l)
l2 = []
for i in range(m):
    x = l[i] / n
    x = Decimal(str(x))
    x = x.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    x = int(x) * n
    if x == 0:
        x = n
    l2.append(x)
for i in l2:
    print(i)