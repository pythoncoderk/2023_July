import math

n = int(input())
l = [int(input()) for i in range(n)]

print(n)
print(l)
all_total = 0
for i in range(n):
    total = 0
    if l[i] >= 1500001:
        total += math.ceil((l[i] - 1500000) * 0.4)
        total += ((1500000-750000) * 0.2)
        total += ((7500000-100000) * 0.1)
    elif l[i] >= 750001:
        total += math.ceil((l[i] - 750000) * 0.2)
        total += ((7500000-100000) * 0.1)
    elif l[i] >= 100001:
        total += math.ceil((l[i] - 100000) * 0.1)
    all_total += total
print(all_total)