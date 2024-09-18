x, y = map(int, input().split())

a = (x + 1) * y
b = (y + 1) * x

if a == b:
    print(a)
elif a > b:
    print(a)
else:
    print(b)