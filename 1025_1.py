d, s = map(int, input().split())
d *= 1000 * 100
if d / s >= 10000:
    print("yes")
else:
    print("no")