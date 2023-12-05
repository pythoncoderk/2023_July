import numpy as np

n = int(input())
l = list(map(int, input().split()))
arr1 = np.array(l)
print(f"{arr1.max()} {arr1.min()}")