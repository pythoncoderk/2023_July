n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)


def tax1(x):
    total = 0
    x -= 100000
    x *= 0.1
    total += int(x)
    return total

def tax2(x):
    total = 65000
    x -= 750000
    x *= 0.2
    total += int(x)
    return total

def tax3(x):
    total = 65000 + 150000
    x -= 1500000
    x *= 0.4
    total += int(x)
    return total

total2 = 0
for i in range(n):
    if 100000 < l[i] <= 750000:
        total2 += tax1(l[i])
    elif 750000 < l[i] <= 1500000:
        total2 += tax2(l[i])
    elif l[i] >= 1500000:
        total2 += tax3(l[i])

print(total2)