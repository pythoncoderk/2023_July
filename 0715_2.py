m, n = map(int, input().split())

count = 0
for i in range(1, m):
    for j in range(1, n):
        x = (i ** 2 + j ** 2) ** 0.5
        if x.is_integer():
            count += 1

print(count)