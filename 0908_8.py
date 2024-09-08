y, x, d = map(str, input().split())
y = int(y)
x = int(x)

d2 = input()

if d == "N":
    if d2 == "R":
        x += 1
    else:
        x -= 1
elif d == "S":
    if d2 == "R":
        x -= 1
    else:
        x += 1
elif d == "E":
    if d2 == "R":
        y += 1
    else:
        y -= 1
else:
    if d2 == "R":
        y -= 1
    else:
        y += 1



print(y, x)
