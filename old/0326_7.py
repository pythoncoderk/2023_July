import math

n, x, y = map(int, input().split())
# print(n, x, y)

print(int(math.ceil(n / x) * y))