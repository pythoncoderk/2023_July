n, k = map(int, input().split())
for i in range(k):
    for j in range(n):
        if j == n-1:
            print(j+1)
        else:
            print(j+1, end=" ")