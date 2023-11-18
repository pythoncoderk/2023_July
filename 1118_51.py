x, y = map(int, input().split())
z = 0
if x >= 5:
    z += 5
else:
    z += x
if y >= 5:
    z += 5
else:
    z += y
print(z)