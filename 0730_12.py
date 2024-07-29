n, m = map(int, input().split())
l = list(map(int, input().split()))
l2 = list(map(int, input().split()))

count = 0
for i in range(m):
    for j in range(l2[i]):
        if j == l2[i] - 1:
            print(l[count])
        else:
            print(l[count], end=" ")
        count += 1