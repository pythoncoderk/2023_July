n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])
l = sorted(l, key=lambda x: x[1])
# print(l)
for i in range(n):
    print(f"{l[i][0]} {l[i][1]} {l[i][2]} {l[i][3]}")
