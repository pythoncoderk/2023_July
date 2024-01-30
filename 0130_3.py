n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
# print(l)
for i in range(n):
    x = l[i][0] - (l[i][1] * 5)
    if x < 0:
        x = 0
    if x >= m:
        print(i+1)