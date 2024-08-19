import math

n, k = map(int, input().split())

x = n // k
y = math.ceil(n / k)

print(abs(x - y))