l = [100, 2, 5, 1, 4, 6, 3]

for i in range(len(l)):
    min_l = l[i]
    index_l = i
    for j in range(i, len(l)):
        if min_l > l[j]:
            min_l = l[j]
            index_l = j
    l[index_l], l[i] = l[i], l[index_l]

print(l)