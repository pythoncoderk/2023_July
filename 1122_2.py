x, y = map(int, input().split())
a, b = map(int, input().split())

if x + y < a + b:
    print(x + y)
else:
    print(a + b)