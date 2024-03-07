m, p, q = map(int, input().split())

# print(m, p, q)

m -= m * (p / 100)
m -= m * (q / 100)


print(m)