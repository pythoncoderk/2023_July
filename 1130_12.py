import numpy as np

arr21 = np.array([[1,2,3],[4,5,6]])
print(np.flip(arr21))

print(arr21[::-1,::-1])

arr22 = np.array([[1,2,3],[4,5,6]])
print(arr22.transpose())

arr23 = np.array([1,2,3])
print(np.append(arr23, 4))
print(np.append(0, arr23))

arr24 = np.arange(6).reshape((2, 3))
print(np.where(arr24<3, True, False))

print(np.where(arr24 < 3))

arr25 = np.arange(6).reshape((2, 3))
print(np.all(arr25 < 6))

arr26 = np.arange(6).reshape((2, 3))
print(np.any(arr26 < 3))

arr27 = np.array([1,2,3])
print(arr27.argmax())

arr28 = np.array([8,2,1,5,6])
print(np.sort(arr28))

arr29 = np.array([8,9,2,1,6,7])
print(np.argsort(arr29))

arr30 = np.arange(6).reshape(2, 3)
print(np.expand_dims(arr30, 0))

print(np.expand_dims(arr30, 0).shape)

print(np.expand_dims(arr30, 1))

print(np.expand_dims(arr30, 1).shape)