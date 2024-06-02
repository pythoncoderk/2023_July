l = [8, 9, 2, 5, 10, 1, 4, 6, 3, 7, 11]

def b_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

print(b_sort(l))