n = int(input())
l = [input() for i in range(n)]
for i in range(n):
    if i == n-1:
        print(l[i])
    else:
        print(l[i], end="")