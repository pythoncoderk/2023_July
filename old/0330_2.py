m, n, x = map(int, input().split())
l = [int(input()) for i in range(m)]
x2 = x
n -= 1

# print(m, n, x)
# print(l)

count = 0
while n != 0 or x != 0:
    if l:
        if x - l[0] > 0:
            x -= l[0]
            l.pop(0)
            count += 1
        else:
            x = 0
            if n >= 1:
                n -= 1
                x = x2
    else:
        break
print(count)