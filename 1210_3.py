import numpy as np

n = int(input())
l = list(map(int ,input().split()))
arr1 = np.array(l)
x = np.where(arr1 % 2 == 0)
print(x[0][0] + 1)
