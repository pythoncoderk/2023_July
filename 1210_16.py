import numpy as np

n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
k = int(input())
for i in range(n):
    l[i][1] = int(l[i][1])
# print(n)
# print(k)
for i in range(n):
    if l[i][1] >= k:
        print(l[i][0])