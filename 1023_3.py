l = []
for i in range(1, 99):
    for j in range(1, 99):
        if i + j <= 100:
            l.append([i, j])
l2 = []
while len(l) != 0:
    if (l[0][0] ** 3) + (l[0][1] ** 3) < 100000:
        l2.append(l[0][0] * l[0][1])
        l.pop(0)
    else:
        l.pop(0)
print(max(l2))
