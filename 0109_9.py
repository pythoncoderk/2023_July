l = [2, 5, 1, 4, 6, 3]
x = 1
l_min = 999
for i in range(len(l)-1):
    for j in range(len(l)-x):
        if l[i] > l[j+x]:
            l_min = l[j+x]
            x += 1
        else:
            x += 1
