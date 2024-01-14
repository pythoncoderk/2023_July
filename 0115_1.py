import math

n = int(input())
l = [int(input()) for i in range(n)]

a = math.floor(750000 * 0.2)
b = math.floor(650000 * 0.1)

l2 = []
for i in range(n):
    if l[i] > 1500000:
        x = l[i] - 1500000
        x = math.floor(x * 0.4)
        l2.append(x + a + b)
    elif l[i] > 750000:
        x = l[i] - 750000
        x = math.floor(x * 0.2)
        l2.append(x + b)
    elif l[i] > 100000:
        x = l[i] - 100000
        x = math.floor(x * 0.1)
        l2.append(x)
print(sum(l2))

