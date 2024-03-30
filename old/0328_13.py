n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, m)
# print(l)

for i in range(n):
    if l[i][0] - (l[i][1] * 5) < 0:
        x = 0
    else:
        x = l[i][0] - (l[i][1] * 5)

    if x >= m:
        print(i+1)