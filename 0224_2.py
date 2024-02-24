l = [7, 2, 5, 8, 3, 4, 6, 9, 10, 1]

for i in range(len(l)):
    min_l = l[i]
    index_l = i
    for j in range(i, len(l)):
        if min_l > l[j]:
            min_l = l[j]
            index_l = j
    l[i], l[index_l] = l[index_l], l[i]

