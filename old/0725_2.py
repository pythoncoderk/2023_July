h, w, n = map(int, input().split())
a = [[int(x) for x in input().split()] for _ in range(h)]

ans = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    ans[i] = [0] + a[i - 1][:]
    for j in range(1, w + 1):
        ans[i][j] += ans[i - 1][j] + ans[i][j - 1] - ans[i - 1][j - 1]

for _ in range(n):
    y, x = map(int, input().split())
    print(ans[y][x])

