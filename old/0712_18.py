from decimal import *

x = Decimal(input())

y = x.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
print(y)