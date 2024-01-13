l = [2, 5, 1, 4, 6, 3]
l_copy = l[::]
l_min = l_copy[0]
while l_copy:
    num = l_copy.pop(0)
    if l_min >= num:
        l_min = num
l_sort = []
l_counts = len(l)-1
counter = 0
i = 0
while l_counts > counter:
    if l[i] == l_min:
        l_sort.append(l.pop(i))
        counter += 1
    else:
        i += 1

