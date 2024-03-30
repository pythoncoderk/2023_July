import math

x, p = map(int, input().split())

coffee = x
discount = 0
total = x
while coffee > 0:
    coffee = coffee - math.ceil(coffee * (p / 100))
    total += coffee

print(total)

