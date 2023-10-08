n = int(input())
l = list(map(int, input().split()))
for i in range(n):
    for j in range(l[i]):
        if j+1 == l[i]:
            print(j+1)
        else:
            print(j+1, end=" ")
