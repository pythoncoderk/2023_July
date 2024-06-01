l = [2, 5, 1, 4, 6, 3]


for i in range(len(l)):
    min_l = l[i]
    min_index = i
    tmp = l[i]
    tmp_index = i
    for j in range(i+1, len(l)):
        if l[j] < min_l:
            min_l = l[j]
            min_index = j
            l[min_index], l[tmp_index] = l[tmp_index], l[min_index]
print(l)





