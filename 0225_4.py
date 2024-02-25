def insert_sort(arr):
    for i in range(1, len(arr)):
        insert(arr, i)

def insert(arr, i):
    tmp = arr[i]
    for j in range(i - 1, -1, -1):
        if tmp < arr[j]:
            arr[j + 1] = arr[j]
        else:
            arr[j + 1] = tmp
            break
    else:
        arr[0] = tmp

org_list = [5, 4, 3, 2, 1]
insert_sort(org_list)
print(org_list)