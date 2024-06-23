l = [2, 5, 1, 4, 6, 3]


def sort_03(arr):
    x = 0
    for i in range(len(arr) - 1, -1, -1):
        for j in range(len(arr) - 1, x, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr

print(sort_03(l))