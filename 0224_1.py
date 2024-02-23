l = [7, 8, 2, 10, 3, 4, 6, 9, 1, 5, 6]

for i in range(len(l)):
    min_l, index_l = l[i], i
    for j in range(i+1, len(l)):
        if min_l > l[j]:
            min_l = l[j]
            index_l = j
    l[index_l], l[i] = l[i], l[index_l]

print(l)

