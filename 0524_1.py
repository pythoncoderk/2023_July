import math

m, d = map(int, input().split())
p, n = map(int, input().split())

# print(m, d)
# print(p, n)

x = n // m
y = n % m
d *= 0.01
total = 0

for i in range(x):
    z = (p - (p * d)) * x