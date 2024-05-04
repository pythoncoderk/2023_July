l = [0, 2, 5, 6, 1, 4, 3, 99]


tmp = max(l)
index_l = max(l)
for i in range(len(l)):
    min_l = max(l)
    for j in range(i, len(l)):
        if l[j] < min_l:
            min_l = l[j]
            tmp = l[i]
            index_l = j
    l[i] = min_l
    l[index_l] = tmp
print(l)