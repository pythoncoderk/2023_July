l = [2, 5, 1, 4, 6, 3]

def o_sort(arr):
    for i in range(len(l)):
        min_l = l[i]
        for j in range(i, len(l)):
            if min_l > l[j]:
                min_l = l[j]
                l[i], l[j] = l[j], l[i]
    return arr

print(o_sort(l))
