import math

x, y, z = map(int, input().split())

t = y / x
s = z * t - 1

if s < 0:
    print(0)
else:
    print(math.ceil(s))
