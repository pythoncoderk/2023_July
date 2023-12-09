import numpy as np

n = int(input())
l = list(map(int, input().split()))
arr1 = np.array(l)
x = np.where(arr1 % 2 == 1)
print(x[-1][-1] + 1)