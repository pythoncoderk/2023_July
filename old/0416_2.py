m, d = map(int, input().split())
p, n = map(int, input().split())

print(m, d)
print(p, n)

discounts = (n // m) * m
print(discounts)

discounts2 = (discounts * p) * (d / 100)
print(discounts2)