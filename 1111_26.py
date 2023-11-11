p, q, r = map(int, input().split())
l_p = [list(map(int, input().split())) for i in range(p)]
l_q = [list(map(int, input().split())) for i in range(q)]

for i in range(q):
    for j in range(p):
        if l_q[i][0] == l_p[j][1]:
            l_p[j].append(l_q[i][1])

l_p = sorted(l_p, key=lambda x: x[0])

for i in range(p):
    print(f"{l_p[i][0]} {l_p[i][2]}")