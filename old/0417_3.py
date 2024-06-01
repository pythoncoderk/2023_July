l = [2, 5, 1, 4, 6, 3]

for i in range(len(l)):
    for j in range(len(l)-1, i, -1):
        if l[j] < l[j-1]:
            min_l = j-1
            max_l = j
            l[max_l], l[min_l] = l[min_l], l[max_l]
print(l)