n, k = map(int, input().split())
l = [int(input()) for i in range(n)]

for i in range(n):
    if l[i] == k:
        print(i + 1)
        exit()

print(-1)