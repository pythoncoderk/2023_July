l_m = [2, 5, 1, 4, 6, 3]
l = l_m[::]
l_min = l[0]

def f_l_min(arr):
    for i in range(len(l)):
        global l_min
        for j in range(i, len(l)):
            if l_min > l[j]:
                l_min = l[j]


f_l_min(l)
print(l_min)
