x, y, p = map(int, input().split())
if x % y == 0:
    z = x // y
else:
    z = (x // y) + 1
print(z * p)