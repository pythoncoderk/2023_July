x, y = map(str, input().split())
x = int(x)
if y == "km":
    print(x * 1000 * 100 * 10)
elif y == "m":
    print(x * 100 * 10)
elif y == "cm":
    print(x * 10)