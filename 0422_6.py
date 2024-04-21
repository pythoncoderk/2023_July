m, p, q = map(int, input().split())

# print(m, p, q)

x = m - ((m * p) / 100)
# print(x)

y = x - ((x * q) / 100)
print(y)
