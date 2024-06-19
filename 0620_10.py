n = int(input())
k = int(input())
x = int(input())
y = int(input())

total = 0
for i in range(1, n + 1):
    if i > k:
        total += y
    else:
        total += x

print(total)