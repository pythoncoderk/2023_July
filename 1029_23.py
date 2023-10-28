n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    print(abs(l[i][0]-2) + abs(l[i][1]-3))
