a, b = map(int, input().split())

if a <= 0 <= b:
    print(a * b)
elif a > 0:
    print(a * a)
else:
    print(b * b)