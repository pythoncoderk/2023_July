import math

x, p = map(int, input().split())
# print(x, p)
total = x
while x > 0:
    x -= math.ceil(x * (p * 0.01))
    total += x
print(total)