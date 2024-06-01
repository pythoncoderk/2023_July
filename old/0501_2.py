m, n = map(int, input().split())

# print(m, n)

count = 0
for i in range(1, m):
    for j in range(1, n):
        for k in range(30 * 30):
            if i ** 2 + j **2 == k ** 2:
                count += 1
print(count)