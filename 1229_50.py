a, b = map(int, input().split())
x, y = map(int, input().split())

if a + b < x + y:
    print(a + b)
else:
    print(x + y)