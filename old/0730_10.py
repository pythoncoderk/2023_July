n, m = map(int, input().split())
l = list(map(int, input().split()))
l2 = list(map(int, input().split()))

for i in range(m):
    for j in range(l2[i]):
        x = l.pop(0)
        if j == l2[i] - 1:
            print(x)
        else:
            print(x, end=" ")
