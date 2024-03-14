x, y, n = map(int, input().split())

# print(x, y, n)

price = 0

if y / 3 < x:
    while n >= 3:
        price += y
        n -= 3
    while n > 0:
        price += x
        n -= 1
else:
    while n > 0:
        price += x
        n -= 1

print(price)