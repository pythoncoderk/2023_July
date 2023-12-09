import numpy
import numpy as np

n = int(input())
l = [int(input()) for i in range(n)]
m = int(input())
l2 = [list(map(int, input().split())) for i in range(m)]
# print(n)
# print(m)
arr1 = np.array(l)
arr2 = np.array(l2)
# print(arr1)
arr2 -= 1
# print(arr2)
counts = 0
arr1_copy = numpy.copy(arr1)
for i in range(m):
    arr1_copy[arr2[i, 0]] -= 1
    arr1_copy[arr2[i, 1]] -= 1
    if arr1_copy[arr2[i, 0]] >= 1 and arr1_copy[arr2[i, 1]] >= 1:
        arr1_copy[arr2[i, 0]] -= 1
        arr1_copy[arr2[i, 1]] -= 1
        counts += 1
print(counts)
