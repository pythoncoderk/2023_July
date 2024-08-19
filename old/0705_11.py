n = int(input())

l = [i for i in range(1, n + 1)]

# print(l)

total = 0
for i in range(1, len(l) + 1):
    total += (10000 * i) / n

print(total)