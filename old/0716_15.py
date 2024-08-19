l = [2, 5, 1, 4, 6, 3]

def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        exchange(arr, i)
    return arr

def exchange(arr, i):
    for j in range(len(arr)-1, i, -1):
        if arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]


x = bubble_sort(l)
print(x)