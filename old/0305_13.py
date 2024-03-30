l = [10, 4, 5, 1, 8, 2, 9, 6, 3, 7]

for i in range(len(l)):
    tmp = l[i]
    for j in range(i, -1, -1):
        if l[j] > tmp:
            l[j+1] = l[j]
            l[j] = tmp
print(l)
