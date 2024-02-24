l = [5, 2, 3, 4, 1, 6, 7, 9, 8]

for i in range(len(l)):
    min_l = l[i]
    index_l = i
    for j in range(i, len(l)):
        if l[j] < min_l:
            min_l = l[j]
            index_l = j
    l[i], l[index_l] = l[index_l], l[i]

print(l)