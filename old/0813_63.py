n = int(input())

x1 = 0
x2 = 1
x3 = 0
for i in range(n):
    if i == 0:
        print(0)
    elif i == 1:
        print(1)
    else:
        print(x1 + x2)
        x1, x2 = x2, x1
        x2 += x1

