import numpy as np

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
arr1 = np.array(l)

# print(n)
# print(arr1)

s = arr1[0][0]
last = arr1[-1][1]
high = np.max(arr1)
lows = np.min(arr1)

print(f"{s} {last} {high} {lows}")