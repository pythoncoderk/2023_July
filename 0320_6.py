from decimal import *


n = Decimal(input())
n = n.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
print(n)

