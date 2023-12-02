import numpy as np

a, b, r = map(int, input().split())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
arr1 = np.array(l)
# print(a, b, r)
# print(n)
for i in range(n):
    if ((arr1[i][0] - a) ** 2) + ((arr1[i][1] - b) ** 2) >= r ** 2:
        print("silent")
    else:
        print("noisy")