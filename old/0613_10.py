m, p, q = map(int, input().split())

x = (m * p) / 100

y = m - x

z = (y * q) / 100

a = y - z

print(a)
