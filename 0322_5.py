l = []
for i in range(36):
    if i <= 1:
        l.append(1)
    else:
        l.append(l[i-2] + l[i-1])
print(l)