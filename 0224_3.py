l = [7, 2, 5, 8, 3, 4, 6, 9, 10, 1]

for i in range(len(l)):
    for j in range(0, i):
        if l[i+1] < l[j]:
            index_l = j
    l.insert(index_l, l.pop(l[i+1]))
