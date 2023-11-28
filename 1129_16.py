import pprint

import numpy as np

n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
m = int(input())
l2 = [list(map(str, input().split())) for i in range(m)]
print(n)
print(l)
print(m)
print(l2)
l = np.array(l)
print(l)
print(np.any(l == l[0][0]))