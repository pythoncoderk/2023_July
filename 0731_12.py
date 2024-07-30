n, a, b = map(int, input().split())
for i in range(n):
    if i == n - 1:
        print("({}, {})".format(a, b))
    else:
        print("({}, {})".format(a, b), end=", ")