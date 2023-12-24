from decimal import Decimal, ROUND_HALF_UP
l = list(map(int, input().split()))
x = Decimal(str(sum(l) / len(l)))
x = x.quantize(Decimal("0.0"), rounding=ROUND_HALF_UP)

print(x)