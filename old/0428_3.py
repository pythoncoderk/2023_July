import math

x, p = map(int, input().split())

# print(x, p)

count = 0
while x > 0:
    count += x
    x = math.floor(x - (x * (p / 100)))

print(count)

