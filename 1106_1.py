n = int(input())
points = list(map(int, input().split()))
l = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(5):
        l[i][j] = l[i][j] * points[j]
l_f = []
for i in l:
    l_f.append(sum(i))

print(max(l_f))