import numpy as np

n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
m = int(input())

arr1 = np.array(l)
# print(n)
# print(m)
# print(arr1)

x = arr1[:, 1]
x_i = x.astype(np.int32)
x_i = np.where(x_i == m)
# print(x_i[0][0])
print(arr1[x_i[0][0]][0])
