n, k = map(str, input().split())
n = int(n)

# print(n, k)

if k == "km":
    print(n * 1000 * 100 * 10)
elif k == "m":
    print(n * 100 * 10)
else:
    print(n * 10)