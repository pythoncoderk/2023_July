n, k = map(int, input().split())

count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        x = k - (i + j)
        if x <= n and x > 0:
            count += 1

print(count)