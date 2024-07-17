def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        exchange(arr, i)


def exchange(arr, i):
    for j in range(len(arr) - 1, i, -1):
        if arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]


l = [9, 8, 7, 6, 5, 4, 3, 2, 1]

bubble_sort(l)
print(l)
