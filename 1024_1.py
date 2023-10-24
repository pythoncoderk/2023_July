x, y, z = map(int, input().split())
a = x
b = y
c = z
counts = 0
if y <= z:
    while y <= z:
        z = z - y
        counts += 1
if x <= z:
    while x <= z:
        z = z - x
        counts += 1
while z != 0:
    z -= 1
    counts += 1
x = a
y = b
z = c
counts2 = 0
if x <= z:
    while x <= z:
        z = z - x
        counts2 += 1
while z != 0:
    z -= 1
    counts2 += 1

if counts > counts2:
    print(counts2)
else:
    print(counts)