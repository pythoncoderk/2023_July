a, b = map(int, input().split())

ans = 999999999999999999999999999999999999999999999999999999
for i in range(a, b + 1):
    x = 0
    for j in range(a, b + 1):
        x = i * j
        if ans > x:
            ans = x

print(ans)