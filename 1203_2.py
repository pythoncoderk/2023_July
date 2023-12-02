import numpy as np

print(np.__version__)
np.show_config()

z = np.zeros(10)
print(z)

z2 = np.zeros((10, 10))
print("%d bytes" % (z2.size * z2.itemsize))

z3 = np.zeros(10)
z3[4] = 1
print(z3)

z4 = np.arange(10, 50, 1)
print(z4)

z5 = np.arange(1, 10)
print("z5", z5)
z5_reverse = z5[::-1]
print(z5_reverse)

z6 = np.arange(0, 9)
z6 = np.reshape(z6,(3, 3))
print(z6)

z7 = np.array([1,2,0,0,4,0])
print(np.nonzero(z7))