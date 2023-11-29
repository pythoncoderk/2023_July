import numpy as np

arr1 = np.array([1, 2, 3])
print(arr1)

arr2 = np.array([4, 5, 6])
print(arr2)

print(arr1 + arr2)

arr3 = np.array([[1, 2],[3, 4], [5, 6]])
print(arr3)

print(arr3.shape)

arr4 = np.arange(10)
print(arr4)

arr9 = np.arange(9).reshape(3, 3)
print(arr9)

arr11 = arr9.reshape(-1)
print(arr11)

arr12 = np.zeros(3)
print(arr12)

arr13 = np.zeros([3, 3])
print(arr13)

arr14 = np.ones([3, 4])
print(arr14)

arr15 = np.empty([3, 3])
print(arr15)

arr16 = np.eye(5)
print(arr16)

arr17 = np.random.randn(3, 3)
print(arr17)