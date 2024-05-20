l = [2, 5, 1, 4, 6, 3, 8]

def sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr))[::-1]:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

print(sort(l))