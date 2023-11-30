import numpy as np

arr31 = np.arange(2)
print(np.broadcast_to(arr31,(2,2)))

arr32 = np.arange(3)
arr32_2 = np.arange(3).reshape(3, 1)
print(np.broadcast_arrays(arr32, arr32_2))

arr33 = np.array([1,2,3])
arr33_2 = np.array([4,5,6])

print(arr33 + arr33_2)

print(arr33 - arr33_2)

print(arr33 * arr33_2)

print(arr33 / arr33_2)

print(arr33 ** 2)

arr34 = np.array([1,2,3])
arr34_2 = np.array([4,5,6])

print(np.add(arr34, arr34_2))

print(arr34 - arr34_2)

arr36 = np.array([[1,2,3],[4,5,6]])
print(np.sum(arr36))

print(np.sum(arr36, axis=0))

print(np.sum(arr36, axis=1))

arr37 = np.array([1,2,3])
arr37_2 = np.array([4,5,6])

print(np.multiply(arr37, arr37_2))

arr38 = np.arange(3).reshape(1,3)
arr38_2 = np.arange(3).reshape(3, 1)

print(np.dot(arr38, arr38_2))


arr39 = np.arange(10).reshape(2, 5)
print(np.mean(arr39))


arr40 = np.arange(10).reshape(2, 5)
print(np.std(arr40))