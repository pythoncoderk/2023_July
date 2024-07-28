def select_sort(arr):
    for i in range(0, len(arr) - 1):
        select_min(arr, i)

def select_min(arr, i):
    min = i
    for j in range(i + 1, len(arr)):
        if arr[min] > arr[j]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]


l = [2, 1, 3, 5, 4, 6, 7, 8, 9]
print(select_sort(l))
print(l)