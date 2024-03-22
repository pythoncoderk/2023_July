import math

a, b = map(int, input().split())

dis = b / 100
price = a
while a > 1:
    a -= math.ceil(dis * a)
    price += a
print(price)