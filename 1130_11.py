import numpy as np

arr11 = np.random.normal(5, 1)
print(arr11)

arr12 = np.array(10)
print(np.random.choice(arr12))

arr13 = np.array([[1,2,3],[4,5,6]])
print(arr13.ndim)

arr14 = np.array([[1,2,3],[4,5,6]])
print(arr14.size)

arr15 = np.array([[1,2,3],[4,5,6]])
print(arr15.shape)

arr16 = np.array([[1,2,3],[4,5,6]])
print(arr16.dtype)

arr17 = np.array([1,2,3])
print(arr17[1])

print(arr17[0:2])

arr17_2 = np.array([[1,2,3],[4,5,6]])
print(arr17_2[0,1])

print(arr17_2[:,1])

print(arr17_2[:,[1,2]])

arr18 = np.array([[1,2,3],[4,5,6]])
print(arr18.reshape(3, 2))

arr19 = np.array([[1,2,3],[4,5,6]])
arr19.resize(3, 3)
print(arr19)

arr20 = np.array([[1,2,3],[4,5,6]])
arr20_2 = arr20.ravel()
print(arr20_2[4])