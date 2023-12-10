import numpy as np

n = int(input())
arr1 = np.array([list(map(int, input().split())) for i in range(n)])
arr2 = np.array([list(map(int, input().split())) for i in range(2)])
# print(arr1)
# print(arr2)
x_max = max(arr2[0])
x_min = min(arr2[0])
# print(x_max)
# print(x_min)
#
y_max = max(arr2[1])
y_min = min(arr2[1])
# print(y_max)
# print(y_min)

l2 = []
for i in range(n):
    if arr1[i][0] <= x_max and arr1[i][0] >= x_min and arr1[i][1] <= y_max and arr1[i][1] >= y_min:
        l2.append(1)
print(len(l2))
