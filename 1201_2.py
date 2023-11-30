import numpy as np

m = int(input())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
print(m)
print(n)
print(l)
arr1 = np.array(l)
print(arr1)