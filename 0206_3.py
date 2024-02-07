m, n = map(int, input().split())
print(m, n)
count = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        if (i / 3 == j / 4) or (i / 4 == j / 3):
            count += 1
print(count)