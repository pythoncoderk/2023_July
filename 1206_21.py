import numpy as np

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
k = int(input())
arr1 = np.array(l)
# print(n)
# print(arr1)
# print(k)
answer = 0
for i in range(n):
    x = arr1[i] - arr1[-1]
    xi, yi = x
    if abs(xi) + abs(yi) <= k:
        answer += 1
print(answer)