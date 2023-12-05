import numpy as np

n = list(map(int, input().split()))
arr1 = np.array(n)

print(f"{arr1.max()} {arr1.min()}")