import numpy as np

n = int(input())
l = list(map(int, input().split()))
k = int(input())
arr1 = np.array(l)
if k in l:
    x = np.where(arr1 == k)
    for i in x[0]:
        print(i+1)