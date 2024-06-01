l = [2, 5, 1, 4, 6, 3]

min_l = l[0]
tmp = l[0]
for i in range(len(l)):
    this = l[i]
    this_index = i
    for j in range(i, -1, -1):
        if this < l[j]:
            tmp = l[j]
            tmp_index = j
            l[tmp_index], l[this_index] = l[this_index], l[tmp_index]
            this_index = j
print(l)



