l = [2, 5, 1, 4, 6, 3]

for i in range(len(l)):
    l_min = l[i]
    l_index = i
    for j in range(i, len(l)):
        if l_min > l[j]:
            l_min = l[j]
            l_index = j
    l[i], l[l_index] = l[l_index], l[i]

print(l)

