n = int(input())
l = [int(input()) for i in range(n)]
for i in range(n):
    for j in range(i):
        print(l[i] * l[j])