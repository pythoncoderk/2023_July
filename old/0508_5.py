l = [2, 44, 5, 1, 4, 6, 3, 9, 7, 8, 10, 11, 12, 13, 14, 99]

for i in range(len(l)):
    min_l = max(l)
    index_l = 0
    for j in range(i, len(l)):
        if min_l > l[j]:
            min_l = l[j]
            index_l = j
    if i != len(l)-1:
        l[i], l[index_l] = l[index_l], l[i]

print(l)
