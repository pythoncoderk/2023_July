m, n, x = map(int, input().split())
l = [int(input()) for i in range(m)]
n2 = n-1
x2 = x
# print(m, n2, x2)
# print(l)
gets = 0
counts = 0
while n2 >= 0 and x2 >= 0:
    if x2 > l[0]:
        x2 -= l[0]
        gets += 1
        l.pop(0)
    else:
        if n2 >= 1:
            n2 -= 1
            x2 = x
        else:
            break
print(gets)