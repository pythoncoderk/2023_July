n = int(input())
l = list(map(str, input().split()))
m = int(input())
l2 = [list(map(str, input().split())) for i in range(m)]
# print(l)
# print(l2)
l4 = []
for i in l:
    l3 = []
    for j in range(m):
        if l2[j][0] == i:
            l3.append(int(l2[j][1]))
    l4.append(sum(l3))
# print(l4)
d = {l[i]: l4[i] for i in range(n)}
# print(d)
d2 = sorted(d.items(), key=lambda x:x[1], reverse=True)
for i in range(n):
    print(d2[i][0])