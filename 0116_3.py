l = [5, 6, 7, 1, 2, 3, 4, 9, 9, 2]

for i in range(len(l)):
    min_l = l[i]
    for j in range(i, len(l)):
        if min_l > l[j]:
            min_l = l[j]
            l[i], l[j] = l[j], l[i]
print(l)
