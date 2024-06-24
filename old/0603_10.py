l = []
for i in range(1, 36):
    if i == 1 or i == 2:
        l.append(1)
    else:
        l.append(l[-1] + l[-2])

print(l)