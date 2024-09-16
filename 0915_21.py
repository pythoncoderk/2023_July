l = [2, 5, 1, 4, 6, 3]

for i in range(len(l)):

    for j in range(i, -1, -1):
        if l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]