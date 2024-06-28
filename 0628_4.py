x, p = map(int, input().split())

coffee = x
total = x
while True:
    price = int(coffee - (coffee * (p / 100)))
    total += price
    coffee = price
    if price < 1:
        break
print(total)