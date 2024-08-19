import math

x, p = map(int, input().split())

count = x
while x > 0:
    y = x - math.ceil(x * (p * 0.01))
    count += y
    x = y

print(count)