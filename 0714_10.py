m, n, x = map(int, input().split())
x2 = x
l = [int(input()) for i in range(m)]

# print(m, n, x)
# print(l)
n -= 1
count = 0
while l:
    if x - l[0] > 0:
        x -= l[0]
        count += 1
        l.pop(0)
    else:
        if n >= 1:
            n -= 1
            x = x2
        else:
            break
print(count)