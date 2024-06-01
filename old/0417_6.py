m, d = map(int, input().split())
p, n = map(int, input().split())

# print(m, d)
# print(p, n)

discount_1 = (n // m) * m
discount_2 = discount_1 * p - ((discount_1 * p) * (d / 100))

# print(discount_2)

price = (n - discount_1) * p

print(int(discount_2 + price))


