n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

def tax(x):
    if x >= 1500001:
        x -= 1500000
        y = x * 0.4
        y += 150000
        y += 65000
        return int(y)
    elif 750001 <= x <= 1500000:
        x -= 750000
        y = x * 0.2
        y += 65000
        return int(y)
    elif 100001 <= x <= 750000:
        x -= 100000
        y = x * 0.1
        return int(y)
    else:
        return 0


count = 0
for i in range(n):
    count += tax(l[i])

print(count)
