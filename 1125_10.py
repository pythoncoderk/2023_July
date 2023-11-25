import math

n = int(input())
l = list(map(int, input().split()))
l_copy = l.copy().copy()
print(l)
print(l_copy)
x = 0
l2 = []
l3 = []
for i in range(n):
    for j in range(n-1):
        l2.append(l_copy[j+1])
    l2.append(l_copy[i+1])


