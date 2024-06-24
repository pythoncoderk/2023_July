l = [2, 5, 1, 4, 6, 3]

def s_sort(arr):
    for i in range(len(arr)):
        for j in range(i, -1, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


print(s_sort(l))