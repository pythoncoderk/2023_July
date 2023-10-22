n, m, k = map(int, input().split())
x = 0
while n <= k:
    n = n + m
    x += 1
print(x)