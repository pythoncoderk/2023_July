import numpy as np

n = int(input())
l = list(map(int, input().split()))
m = int(input())
l2 = [int(input()) for i in range(m)]
# print(n)
# print(l)
# print(m)
# print(l2)
arr1 = np.array(l)
arr2 = np.array(l2)

for i in arr2:
    if i in arr1:
        print("Yes")
    else:
        print("No")