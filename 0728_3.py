n = int(input())

x = 0
for i in range(1, n + 1):
    x += (10000 * i) * (1 / n)

print(x)