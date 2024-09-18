l = [2, 5, 1, 4, 6, 3]

for i in range(1, len(l)):
    tmp = l[i]
    for j in range(len(l)):
        if l[j] > tmp:
            l[j + 1] = l[j]
        else:
            l[j] = tmp
            break
    else:
        l[0] = tmp

