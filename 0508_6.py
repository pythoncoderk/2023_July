l = [2, 44, 5, 1, 4, 6, 3, 9, 7, 8, 10, 11, 12, 13, 0, 14, 99]

for i in range(len(l)):
    tmp = 0
    for j in range(i, 0, -1):
        if l[j] < l[j-1]:
            tmp = l[j-1]
            l[j-1] = l[j]
            l[j] = tmp
print(l)

