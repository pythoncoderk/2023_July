l = [2, 5, 1, 4, 6, 3]

def s_sort(arr):
    for i in range(len(arr)):
        min_l = arr[i]
        index_l = i
        for j in range(i-1, -1, -1):
            if min_l < arr[j]:
                arr[index_l], arr[j] = arr[j], arr[index_l]
                min_l = arr[j]
                index_l = j
    return arr


print(s_sort(l))


