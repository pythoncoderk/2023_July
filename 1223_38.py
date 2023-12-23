import math

a, m, l, r = map(int, input().split())

x = abs(a - m)
y = abs(l - r)

if l == r:
    print(0)
else:
    print(math.floor(y / x))