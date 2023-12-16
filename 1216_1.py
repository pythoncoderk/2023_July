l = [5, 3, 1, 9, 6, 2, 7, 4, 8, 10,]

for i in range(len(l)-1):
    for j in range(i, len(l)-1):
        if l[i] > l[j+1]:
            l[i], l[j+1] = l[j+1], l[i]
print(l)
