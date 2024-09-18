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

l = [2, 5, 1, 4, 6, 3]
insert_sort(l)
print(l)
