import numpy as np

n = int(input())
l = list(map(int, input().split()))
m = int(input())
arr1 = np.array(l)
# print(n)
# print(arr1)
# print(m)
print(np.count_nonzero(arr1 == m))