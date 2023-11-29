import numpy as np

arr1 = np.arange(9)
print(arr1)

print(arr1[0])
print(arr1[-1])
print(arr1[-2])
print(arr1[1:4])
print(arr1[2:])

arr2 = np.arange(9).reshape(3, 3)
print(arr2)

print(arr2[0, 0])
print(arr2[0, 1])

print(arr2[:, 1])
print(arr2 > 4)

print(arr2[arr2>4])