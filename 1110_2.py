# coding: utf-8
n = int(input())
l = list(map(int, input().split()))
l2 = l[:1]
for i in range(n-1):
    if l[i+1] in l2:
        print("Yes")
    else:
        print("No")
    l2.append(l[i+1])