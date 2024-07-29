n = int(input())
l = list(map(int, input().split()))

for i in range(n):
    for j in range(1, l[i] + 1):
        if j == l[i]:
            print(j)
        else:
            print(j, end=" ")
