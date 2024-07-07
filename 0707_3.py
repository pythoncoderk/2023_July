n, k = map(int, input().split())
l = [list(map(str, input().split())) for i in range(n)]
l2 = [list(map(str, input().split())) for i in range(k)]

# print(l2)

d = {l[k][0]: l[k][1] for k in range(n)}

# print(d)


for i in range(k):
    if l2[i][0] == "call":
        print(d[l2[i][1]])
    elif l2[i][0] == "leave":
        d["*"] = d.pop(l2[i][1])
    elif l2[i][0] == "join":
        d[l2[i][1]] = l2[i][2]