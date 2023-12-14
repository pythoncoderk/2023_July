import numpy as np

arr = np.arange(9).reshape((3,3))
print(arr)

print(arr.T)

print(arr.transpose(0,1))

print(arr.transpose(1,0))

print(arr.swapaxes(1,0))

print(np.dot(arr.T, arr))
