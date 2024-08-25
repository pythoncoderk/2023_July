n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    x = l[i][0]
    l2 = l[i][1:]
    print(sum(l2))

