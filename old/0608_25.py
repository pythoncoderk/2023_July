a, b, c = map(int, input().split())

if c - (a - b) >= 1:
    print(c - (a - b))
else:
    print(0)