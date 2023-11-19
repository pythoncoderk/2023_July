x, y = map(int, input().split())
if x > 0 and y > 0:
    print(x - y)
elif x > 0 and y < 0:
    print(x + abs(y))
elif x < 0 and y < 0:
    print(abs(y) - abs(x))