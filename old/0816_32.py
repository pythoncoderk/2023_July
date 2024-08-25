n, k = map(int, input().split())

# print(n, k)

count = 0
while n < k:
    n *= 2
    count += 1

print(count)