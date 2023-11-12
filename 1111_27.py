x = 10000
y = 0
while y == 0:
    if x % 13 == 0:
        print(x)
        y += 1
        break
    else:
        x += 1