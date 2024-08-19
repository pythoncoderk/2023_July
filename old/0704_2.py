n, k = map(int, input().split())

l = [i for i in range(1, n + 1)]

# print(l)

count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        x = k - (i + j)
        if 1 <= x <= n:
            count += 1

print(count)