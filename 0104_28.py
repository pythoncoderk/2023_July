n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
x, y = map(int, input().split())
a, b = map(int, input().split())
counts = 0
for i in range(n):
    if l[i][0] >= x and l[i][0] <= y and l[i][1] >= a and l[i][1] <= b:
        counts += 1
print(counts)