from decimal import *

l = list(map(int, input().split()))
sum_l = Decimal(str(sum(l) / len(l)))

d_sum_l = sum_l.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
print(d_sum_l)