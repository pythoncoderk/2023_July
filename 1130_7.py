import numpy as np

arr1 = np.arange(10).reshape(5, 2)
print(arr1)

print(arr1.mean())

print(arr1.mean(axis=0))
print(arr1.mean(axis=1))

print(arr1.std())

print(arr1.std(ddof=1))

arr2 = np.random.randn(100)
print(arr2)

print(arr2.max())
print(arr2.min())

print(np.sort(arr2))

print(np.where(arr2 > 0, 1, -1))

print(np.where(arr2 > 0))
print(arr2[np.where(arr2 > 0)])

arr3 = np.array([1, 2, 3, 1, 3, 1, 4, 4, 4])
arr4 = np.unique(arr3)
print(arr4)