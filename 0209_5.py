from decimal import Decimal, ROUND_HALF_UP

n, m = map(int, input().split())
l = [int(input()) for i in range(m)]
# print(n, m)
# print(l)

for i in range(m):
    if l[i] < n:
        print(n)
    else:
        x = l[i] / n
        x2 = Decimal(str(x)).quantize(Decimal("0"), ROUND_HALF_UP)
        print(x2 * n)


