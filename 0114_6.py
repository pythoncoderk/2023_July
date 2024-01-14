l = [5, 3, 1, 9, 6, 2, 7, 4, 8, 10]

for i in range(len(l)):
    min_l = l[i]
    for j in range(i, len(l)):
        if min_l > l[j]:
            l[j], l[i] = l[i], l[j]
            min_l = l[i]

print(l)

