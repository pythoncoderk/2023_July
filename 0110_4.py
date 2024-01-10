n = int(input())
l2 = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l2[i][1] = int(l2[i][1])
d = {l2[k][0]: l2[k][1] for k in range(n)}
d2 = sorted(d.items(), key=lambda x:x[1], reverse=True)
print(d2[1][0])