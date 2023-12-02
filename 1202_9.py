import numpy as np

a = np.array([1,2,3])
print(a)

print(a[1])

a = np.array([[1,2,3],[4,5,6]])

print(a)

print(a[0])

print(a.shape)

print(a.dtype)

print(a.size)

b = np.arange(0, 30, 5)
print(b)

c = np.arange(0, 2, 0.3)
print(c)

d = np.zeros([3, 4])
print(d)