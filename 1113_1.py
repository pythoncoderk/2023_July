l = [2, 5, 1, 4, 6, 3]
l2 = []
while l != []:
    x = min(l)
    y = l.index(x)
    z = l.pop(y)
    l2.append(z)
print(l2)