m, n, x = map(int, input().split())
l = [int(input()) for i in range(m)]

# print(m, n, x)
# print(l)
x1 = x
count = 0
while n > 0:
    if x - l[0] > 0:
        x -= l[0]
        count += 1
        l.pop(0)
    else:
        if n > 1:
            x = x1
            n -= 1
        else:
            break
print(count)
