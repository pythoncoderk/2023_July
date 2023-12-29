from decimal import Decimal, ROUND_HALF_UP
import numpy as np

x, y, z = map(int, input().split())
l1 = list(map(float, input().split()))
l2 = [list(map(int, input().split())) for i in range(y)]

arr1 = np.array(l1)
arr2 = np.array(l2)

# print(x, y, z)
# print(arr1)
# print(arr2)
l3 = []
for i in range(y):
    l3.append(sum(arr1 * arr2[i]))
l4 = []
for i in l3:
    i = Decimal(str(i))
    i = i.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    l4.append(i)
l4.sort(reverse=True)
# print(l4)

for i in range(z):
    print(l4[i])