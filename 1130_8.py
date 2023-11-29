import numpy as np

# arr1 = np.array(list(map(int, input().split()))).reshape((1, 2))
# print(arr1)

# arr1 = np.array(list(map(int, input().split()))).reshape(1, 2)
# print(arr1)
#
# print(arr1.max())

arr2 = np.array(list(map(int, input().split()))).reshape(1, 2)
if arr2[0][0] > arr2[0][1]:
    print(arr2[0][0])
elif arr2[0][0] == arr2[0][1]:
    print("eq")
else:
    print(arr2[0][1])