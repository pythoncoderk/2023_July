x, y = map(str, input().split())
x = list(x)
y = list(y)
z = x + y

if z.count(z[0]) == len(z):
    print("Yes")
else:
    print("No")