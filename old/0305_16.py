n, k, q = map(int, input().split())
l = [int(input()) for i in range(n)]

for i in range(n):
    if i == k:
        print(q)
        print(l[i])
    else:
        print(l[i])