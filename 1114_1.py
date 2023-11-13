n, m = map(str, input().split())
if m == "km":
    x = int(n) * 1000 * 100 * 10
elif m == "m":
    x = int(n) * 100 * 10
else:
    x = int(n) * 10

print(x)