n, r = map(int, input().split())

if n >= 10:
    print(r)
else:
    x = 100 * (10 - n)
    print(r + x)