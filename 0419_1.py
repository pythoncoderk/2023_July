a, b = map(int, input().split())

if a > b * 0.7:
    print(int(b * 0.7))
else:
    print(a)