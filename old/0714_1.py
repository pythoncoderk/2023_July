import math

x, y = map(int, input().split())

if x >= y:
    print(0)
    exit()

z = y - x

print(math.ceil(z / 10))