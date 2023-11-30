import numpy as np

x, y, z = map(int, input().split())

arr1 = np.array(list(map(float, input().split())))
l = [list(map(int, input().split())) for i in range(y)]
arr2 = np.array(l)
print(arr2)
for i in range(y):
    print(arr1 + arr2)