import sys

n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
l3 = [i+1 for i in range(n)]
l2 = []
for i in range(n):
    for j in range(n):
        if l[i][j] >= m:
            l2.append(j+1)
final = list(set(l3) - set(l2))
if final == []:
    print("wait")
    sys.exit()
for i in range(len(final)):
    if i == len(final)-1:
        print(final[i])
    else:
        print(final[i], end=" ")