l = [5, 6, 7, 8, 9, 4, 3, 2, 1]

for i in range(len(l)):
    min_l = l[i]
    for j in range(i, len(l)):
        if min_l > l[j]:
            min_l = l[j]
            l[j] = l[i]
            l[i] = min_l
print(l)