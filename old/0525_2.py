m, d = map(int, input().split())
p, n = map(int, input().split())

# print(m, d)
# print(p, n)

d_price = p - (p * (d * 0.01))
# print(d_price)

d_i = (n // m) * m
# print(d_i)

n_i = n - d_i
# print(n_i)

x = d_i * d_price
y = n_i * p

print(int(x + y))