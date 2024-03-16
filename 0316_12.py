x = int(input())
x2 = x // 10
x3 = x % 10

if 1 <= x3 <= 9:
    print(x2 + 1)
else:
    print(x2)