m, p, q = map(int, input().split())

print(m, p, q)

x = m * (p / 100)
y = m - x

z = y * (q / 100)
az = y - z

print(az)