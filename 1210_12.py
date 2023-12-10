import numpy as np

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
k = int(input())
# print(n)
arr1 = np.array(l)
# print(arr1)
x = arr1[-1]
y = x - arr1
z = abs(y)
# print(z)
aa = np.sum(z, axis=1)
# print(aa)
bb = np.where(aa <= k)
print(len(np.unique(bb)))
