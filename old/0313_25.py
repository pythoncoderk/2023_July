from decimal import *
a, b = map(int, input().split())

x = str(b / a)
x = Decimal(x)
x = x.quantize(Decimal(".001"), rounding=ROUND_HALF_UP)
print(x)
