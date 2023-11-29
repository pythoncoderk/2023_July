import numpy as np

n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
m = int(input())
l2 = [list(map(str, input().split())) for i in range(m)]
print(n)
print(m)
for i in range(n):
    l[i][1] = int(l[i][1])
for i in range(m):
    l2[i][1] = int(l2[i][1])
print(l)
print(l2)

a = np.array(l)
print(a)