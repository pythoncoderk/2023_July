import numpy as np

n = int(input())
l = list(map(int, input().split()))
k = int(input())
arr1 = np.array(l)
x = np.where(arr1[arr1 >= k])
print(x)