m, n, x = map(int, input().split())
l = [int(input()) for i in range(m)]
x1 = x
# print(m, n, x)
# print(l)
count = 0
while l:
    if x <= l[0]:
        x = 0
        if n > 1:
            n -= 1
            x = x1
        else:
            break
    else:
        x -= l[0]
        count += 1
        l.pop(0)
print(count)