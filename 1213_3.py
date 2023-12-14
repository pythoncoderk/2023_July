def select_sort(arr):
    for i in range(0, len(arr)-1):
        select_min(arr, i)
def select_min(arr, i):
    min = i
    for j in range(i + 1, len(arr)):
        if arr[min] > arr[j]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]

org_list = [17, 11, 12, 5, 14]
select_sort(org_list)
print(org_list)