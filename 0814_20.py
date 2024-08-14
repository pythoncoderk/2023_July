n, m = map(int, input().split())
l = [int(input()) for i in range(n)]
for i in range(m):
    if i + 1 <= n:
        print(l[i])
    else:
        print(0)