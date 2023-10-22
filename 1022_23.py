n = int(input())
l = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if j == n-1:
            print(l[i] * l[j])
        else:
            print(l[i] * l[j], end=" ")