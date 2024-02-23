import math

a, b = map(int, input().split())

x = b - a
print(math.ceil(x / a) + 1)