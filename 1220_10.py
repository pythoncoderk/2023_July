l = [2, 5, 1, 4, 6, 3]
l2 = []
l2.append(l.pop(0))

for i in range(len(l)-1):
    x = l.pop(0)
    for j in range(len(l2)):
        if x < l2[i]:
            l2.insert(i, x)
            break
    l2.append(x)