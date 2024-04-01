m, n = map(int, input().split())

l = []
x = 0
y = 1
while len(l) < m:
    if 0 <= x + y <= 99:
        z = f"{x} + {y} ="
        if z not in l:
            l.append(z)
            y += 1
        if y >= 10:
            y = 0
            x += 1

x = 0
y = 99
while len(l) < m + n:
    if 0 <= y - x <= 99:
        z = f"{y} - {x} ="
        if z not in l:
            l.append(z)
            y -= 1
        if y == 0:
            y = 99
            x += 1

for i in l:
    print(i)