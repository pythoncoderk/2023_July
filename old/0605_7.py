a, b = map(int, input().split())


if (a * 2 + 100) - b > 0:
    print((b - (a * 2 + 100)) * -1)
else:
    print(0)