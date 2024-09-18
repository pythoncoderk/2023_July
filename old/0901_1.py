p, q, r = map(int, input().split())
l = [list(map(int, input().split())) for i in range(p)]
l2 = [list(map(int, input().split())) for i in range(q)]

d = {l[i][0]: l[i][1] for i in range(p)}
d2 = {l2[i][0]: l2[i][1] for i in range(p)}
d_final = {i + 1: 0 for i in range(r)}

print(d)
print(d2)

for i in range(p):
    d2[l[i][0]] = l[i][1]

for i in range(q):
    d_final[l2[i][0]] = d2[l2[i][0]]
l.sort()
for i in range(p):
    print(l[i][0], d_final[l[i][0]])