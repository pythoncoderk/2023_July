n, m = map(int, input().split())

if n < 0 and m < 0:
    print(abs(n) + abs(m))
elif n > 0 and m > 0:
    print(n - m)
else:
    print(n + abs(m))