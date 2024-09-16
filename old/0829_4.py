n = int(input())
l = [int(input()) for i in range(n)]
k = int(input())

for i in range(n):
    if k == l[i]:
        print(i + 1)
        break