n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
xs, xt = map(int, input().split())
ys, yt = map(int, input().split())

count_l = 0
for i in range(n):
    if l[i][0] >= xs and l[i][0] <= xt and l[i][1] >= ys and l[i][1] <= yt:
        count_l += 1

print(count_l)


