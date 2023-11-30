from decimal import Decimal, ROUND_HALF_UP
import numpy as np

n, m, k = map(int, input().split())
arr1 = np.array(list(map(float, input().split())))
l = [list(map(int, input().split())) for i in range(m)]
arr2 = np.array(l)
# print(n, m, k)
# print(arr1)
# print(arr2)
l2 = []
for i in range(m):
    l2.append(Decimal(sum(arr2[i] * arr1)).quantize(Decimal("0"), ROUND_HALF_UP))
l2.sort(reverse=True)
# print(l2)
for i in range(k):
    print(l2[i])

