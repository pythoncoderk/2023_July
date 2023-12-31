m, p, q = map(int, input().split())

x = m * (p * 0.01)
m -= x

x = m * (q * 0.01)
m -= x

print(m)