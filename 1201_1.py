import math
import numpy as np

m = int(input())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
# print(m)
# print(n)
# print(l)
arr1 = np.array(l)
# print(arr1)
counts = list(set(arr1[:, 0]))
# print(counts)
l2 = []
for i in range(len(counts)):
    l3 = []
    for j in range(n):
        if counts[i] == l[j][0]:
            l3.append(l[j][2])
    l2.append(math.ceil(sum(l3)/m))
print(sum(l2))
