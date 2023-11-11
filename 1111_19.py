n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
l2 = sorted(l, key=lambda x:(x[0], x[1]), reverse=True)
for i in range(n):
    print(f"{l2[i][0]} {l2[i][1]}")