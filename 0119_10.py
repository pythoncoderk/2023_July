m, n = map(int, input().split())
l2 = [list(map(int, input().split())) for i in range(m)]
l1 = list(map(int, input().split()))

for i in range(m):
    if l2[i] == l1:
        print(i + 1)