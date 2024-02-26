n, m = map(str, input().split())
n = int(n)

if m == "km":
    print(n * 1000 * 100 * 10)
elif m == "m":
    print(n * 100 * 10)
elif m == "cm":
    print(n * 10)