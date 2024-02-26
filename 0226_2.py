l = [2, 5, 1, 4, 6, 3]

for i in range(len(l)):
    tmp = i
    for j in range(i, 0, -1):
        if l[i] > l[j]:
            l[j] = l[i]
            l[i] = tmp

