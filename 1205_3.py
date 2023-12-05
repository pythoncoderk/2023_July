import numpy as np

n = int(input())
l = list(map(int, input().split()))
m = int(input())
arr1 = np.array(l)

if m in l:
    x = np.where(arr1 == m)
    print(x[0][-1] + 1)
else:
    print(0)