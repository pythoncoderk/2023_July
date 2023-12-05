import numpy as np

n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
m = input()
arr1 = np.array(l)
print(n)
print(m)
print(arr1)
print(np.where(arr1 == m))