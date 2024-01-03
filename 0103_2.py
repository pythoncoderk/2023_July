from decimal import Decimal, ROUND_HALF_UP

x, y = map(int, input().split())
l = [int(input()) for i in range(y)]
# print(x, y)
# print(l)
for i in l:
    orange = Decimal(str(i / x))
    orange = orange.quantize(Decimal("0"), rounding=ROUND_HALF_UP) * x
    if orange < x:
        print(int(x))
    else:
        print(int(orange))
