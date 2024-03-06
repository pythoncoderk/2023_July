l = [7, 4, 1, 8, 2, 5, 9, 3, 6]

for i in range(len(l)):
    for j in range(len(l)-1, i, -1):
        if l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]
print(l)