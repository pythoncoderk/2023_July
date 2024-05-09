l = [17, 11, 12, 5, 14, 9, 6, 16, 4, 10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def merge(arrf, arrb):
    if len(arrf) < 1:
        return arrb
    if len(arrb) < 1:
        return arrf
    if arrf[0] <= arrb[0]:
        return [arrf[0]] + merge(arrf[1:], arrb)
    else:
        return [arrb[0]] + merge(arrf, arrb[1:])


print(merge_sort(l))
print(l)