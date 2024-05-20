l = [2, 5, 1, 4, 6, 3, 8]

def sort(arr):
    for i in range(len(arr)):
        min_l = 9999
        index_l = 9999
        for j in range(i, len(arr)):
            if arr[j] < min_l:
                min_l = arr[j]
                index_l = j
        arr[i], arr[index_l] = arr[index_l], arr[i]
    return arr


print(sort(l))