n = int(input())
l = list(map(str, input().split()))
for i in range(n):
    if i == n-1:
        print(l[i][0])
    else:
        print(l[i][0], end="")