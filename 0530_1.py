n, k = map(int, input().split())

# print(n, k)

l = [i for i in range(1, n + 1)]

min_l = min(l)
max_l = max(l)

count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if min_l <= k - (i + j) <= max_l:
            count += 1

print(count)