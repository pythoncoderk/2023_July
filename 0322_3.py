l = [5, 9, 6, 1, 2, 7, 3, 8, 4]

for i in range(len(l)-1):
    target = l[i+1]
    for j in range(i, -1, -1):
        if l[j] > target:
            tmp = l[j]
            l[j] = target
            l[j+1] = tmp
print(l)

