l = [2, 5, 1, 4, 6, 3]
min_l = l[0]
x = l[0]
for i in range(len(l)-1):
    for j in range(i, len(l)):
        if min_l > l[j]:
            min_l = l[j]
            l[j] = x
            l[i] = min_l
            x = min_l


