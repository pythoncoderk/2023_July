n = int(input())
l = list(map(int, input().split()))
m = int(input())
l2 = [list(map(int, input().split())) for i in range(m)]

# print(n)
# print(l)
# print(m)
# print(l2)

ok = []
o = 0
for i in range(n+1):
    if i == 0:
        ok.append(0)
    else:
        if l[i-1] == 1:
            o += 1
            ok.append(o)
        else:
            ok.append(o)

ng = []
g = 0
for i in range(n+1):
    if i == 0:
        ng.append(0)
    else:
        if l[i-1] == 0:
            g += 1
            ng.append(g)
        else:
            ng.append(g)

# print(ok)
# print(ng)

for i in range(m):
    oks = ok[l2[i][1]] - ok[l2[i][0]-1]
    ngs = ng[l2[i][1]] - ng[l2[i][0]-1]
    if oks == ngs:
        print("draw")
    elif oks > ngs:
        print("win")
    else:
        print("lose")
