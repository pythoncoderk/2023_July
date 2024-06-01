n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, m)
# print(l)

for i in range(n):
    x = l[i][1] * 5
    if l[i][0] - x < 0:
        y = 0
    else:
        y = l[i][0] - x
    if y >= m:
        print(i+1)
