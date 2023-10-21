n, m = map(int, input().split())
x = 0
while n % m == 0:
    n = n / m
    x += 1
print(x)