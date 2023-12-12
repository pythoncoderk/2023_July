import numpy as np

h, w = map(int, input().split())
n, t = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
print(h, w)
print(n, t)
x = n-1
l2 = []
for i in range(n-1):
    counts = 0
    for j in range(x):
        print(l[i][0])
        if l[i][0] == l[i+1][0] and l[i][1] == l[i+1][1]:
            counts += 1
    l2.append(counts)
