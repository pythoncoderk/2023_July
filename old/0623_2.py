l = [2, 5, 1, 4, 6, 3]


def sort_02(arr):
    for i in range(len(arr)):
        min_l = arr[i]
        min_l_index = i
        for j in range(i, -1, -1):
            if arr[i] < arr[j]:
                min_l = arr[j]
                min_l_index = j
        x = arr.pop(i)
        arr.insert(min_l_index, x)

    return arr

print(sort_02(l))



