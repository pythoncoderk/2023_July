n, k = map(int, input().split())
l = [int(input()) for i in range(n)]

for i in l:
    if i >= k:
        print(i)