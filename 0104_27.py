n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
k = int(input())
l2 = []
for i in range(n):
    x = abs(l[i][0] - l[-1][0]) + abs(l[i][1] - l[-1][1])
    if x <= k:
        l2.append(x)
print(len(l2))