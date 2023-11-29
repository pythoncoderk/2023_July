import numpy as np

arr1 = np.array([1, 2, 3])
print(arr1)

arr2 = np.zeros(3, dtype=float)
print(arr2)

arr3 = np.array([1, 2, 3])
arr35 = np.zeros_like(arr3)
print(arr35)

arr4 = np.ones(3)
print(arr4)

arr5 = np.eye(5)
print(arr5)

arr6 = np.arange(0, 2, 0.5)
print(arr6)

arr7 = np.linspace(1, 9, 3)
print(arr7)

arr8 = np.random.rand(2)
print(arr8)

arr8_2 = np.random.rand(2, 2)
print(arr8_2)

arr9 = np.random.randint(1, 7)
print(arr9)

arr10 = np.random.randn()
print(arr10)

arr10_2 = np.random.randn(2, 2)
print(arr10_2)
