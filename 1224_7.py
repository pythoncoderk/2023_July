import math

x, y, z = map(int, input().split())
g = math.ceil(x / y) * z
print(g)