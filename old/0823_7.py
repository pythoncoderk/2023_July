n = int(input())

total = 0
for i in range(1, n - 1):
    total += i * (i + 1)

print(total)

count = 0
while total % 2 == 0:
    total /= 2
    count += 1

print(count)