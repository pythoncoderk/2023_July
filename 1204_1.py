import numpy as np

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
# print(n)
arr1 = np.array(l)
# print(arr1)
arr1 = sorted(arr1, key=lambda x: (x[0],x[1],x[2]))[::-1]

# print(arr1)
for i in range(n):
    print(f"{arr1[i][0]} {arr1[i][1]} {arr1[i][2]}")