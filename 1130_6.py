import numpy as np

arr1 = np.loadtxt("./brownian_x.csv", delimiter=",", skiprows=1)
print(arr1)

print(arr1.shape)
np.savetxt("./test.csv", arr1, delimiter=",")