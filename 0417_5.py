l = []
x = 0
y = 0
for i in range(1, 36):
    if i == 1:
        l.append(1)
    else:
        if i <= 2:
            l.append(1)
            x += 1
        else:
            l.append(l[y] + l[y+1])
            y += 1
print(*l)