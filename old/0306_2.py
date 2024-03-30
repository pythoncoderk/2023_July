a, b = map(int, input().split())

count = 0
y = 1
while y < b:
    y += a - 1
    count += 1
print(count)