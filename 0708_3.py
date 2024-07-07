import math

k = int(input())

x = math.ceil(k / 2)

# print(x)

total = 0
for i in range(1, x + 1):
    if i == x:
        if k % 2 == 0:
            total += i
        else:
            pass
    else:
        total += i
        total += i

print(total)

