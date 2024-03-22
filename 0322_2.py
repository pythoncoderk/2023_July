l = [5, 9, 6, 1, 2, 7, 3, 8, 4]

for i in range(len(l)):
    min_l = l.index(l[i])
    index_l = l.index(l[i])
    for j in range(i, len(l)):
        if l[min_l] > l[j]:
            min_l = l.index(l[j])
    l[min_l], l[index_l] = l[index_l], l[min_l]
print(l)

