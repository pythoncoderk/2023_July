l = [2, 5, 1, 4, 6, 3]


def sorts_01(arr):
    for i in range(len(arr)):
        min_l = arr[i]
        index_l = i
        for j in range(i, len(arr)):
            if arr[j] < min_l:
                min_l = arr[j]
                index_l = j
        arr[i], arr[index_l] = arr[index_l], arr[i]
    return arr

print(sorts_01(l))
