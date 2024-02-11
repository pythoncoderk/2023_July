n = input()
while True:
    x = n[::-1]
    y = int(x) + int(n)
    y2 = str(y)
    y3 = str(y)[::-1]
    n = y2
    if y2 == y3:
        print(n)
        break
