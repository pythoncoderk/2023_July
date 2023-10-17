x, y = map(int, input().split())
if x > 0 and y > 0:
    print(x * x)
elif x < 0 and y < 0:
    print(y * y)
elif y == 0 or x == 0:
    print(0)
elif x < 0 and y > 0:
    print(x * y)

