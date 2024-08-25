n, m = map(int, input().split())

ans = 0
i = 0
while n > 0:
    x = n // m
    y = n % m
    ans += y * (10 ** i)
    n = x
    i += 1


print(ans)