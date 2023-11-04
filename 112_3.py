x, y = map(str, input().split())
x = list(x)
y = list(y)
z = x + y
if len(z) == z.count(z[0]):
    print("Yes")
else:
    print("No")