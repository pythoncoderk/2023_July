from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

n = int(input())

l = [10000 * i for i in range(1, n + 1)]

# print(l)

l2 = []
for i in range(n):
    x = l[i] * (1 / n)
    x = Decimal(str(x)).quantize(Decimal("0"), ROUND_HALF_UP)
    l2.append(x)

print(sum(l2))