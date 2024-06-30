l = [2, 5, 1, 4, 6, 3]

def sort_01(arr):
    for i in range(len(arr)):
        min_l = l[i]
        index_l = i
        for j in range(i, len(arr)):
            if min_l > l[j]:
                min_l = l[j]
                index_l = j
        l[i], l[index_l] = l[index_l], l[i]
    return arr

print(sort_01(l))
