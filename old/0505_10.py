n, kk = map(int, input().split())

count = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        x = kk - i - j
        if 1 <= x <= n:
            count += 1

print(count)