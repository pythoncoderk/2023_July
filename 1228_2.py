import math

a, b = map(int, input().split())
print(math.floor((a * 0.01) * b) + b)