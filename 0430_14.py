m, n, x = map(int, input().split())
l = [int(input()) for i in range(m)]

x2 = x
poi = 1

# print(m, n, x)
# print(l)

count = 0
fish = l.pop(0)
while True:
    x2 -= fish
    if x2 > 0:
        count += 1
        if l:
            fish = l.pop(0)
        else:
            break
    else:
        if n > poi:
            poi += 1
            x2 = x
        else:
            break
print(count)
