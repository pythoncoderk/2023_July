n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
x1, x2 = map(int, input().split())
y1, y2 = map(int, input().split())
counts = 0

for i in range(n):
    if l[i][0] >= x1 and l[i][0] <= x2 and l[i][1] >= y1 and l[i][1] <= y2:
        counts += 1

print(counts)