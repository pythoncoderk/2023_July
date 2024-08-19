n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

x1 = 2
y1 = 3

for i in range(n):
    x2 = l[i][0]
    y2 = l[i][1]
    print(abs(x1 - x2) + abs(y1 - y2))
