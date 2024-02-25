m, d = map(int, input().split())
p, n = map(int, input().split())

# print(m, d)
# print(p, n)

x = (n // m) * m
y = n % m

# print(x)
# print(y)

x = (p * x) - ((p * x) * (d * 0.01))
y = y * p

print(int(x + y))
