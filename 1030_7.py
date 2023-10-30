n = int(input())
l = [int(input()) for i in range(n)]

x = n-1

for i in range(x):
    for j in range(x):
        print(l[i] * l[i+j+1])
