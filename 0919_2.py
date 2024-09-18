from decimal import Decimal, ROUND_HALF_UP

n, m = map(int, input().split())
for i in range(m):
    x = int(input())
    y = x / n
    z = Decimal(str(y)).quantize(Decimal("0"), ROUND_HALF_UP) * n
    if z == 0:
        z = n
    print(z)


