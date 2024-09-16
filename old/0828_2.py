n = int(input())
l = [int(input()) for i in range(n)]
k = int(input())

for i in range(n):
    if l[i] == k:
        print(i + 1)
        break