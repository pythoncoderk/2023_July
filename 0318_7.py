n = int(input())
l = list(map(str, input().split()))
m = int(input())
l2 = [list(map(str, input().split())) for i in range(m)]

# print(n)
# print(l)
# print(m)


d = {l[k]: 0 for k in range(n)}
# print(d)

for i in range(m):
    l2[i][1] = int(l2[i][1])
# print(l2)

for i in range(m):
    d[l2[i][0]] += l2[i][1]

ld = list(d.items())
ld = sorted(ld, key=lambda x: x[1], reverse=True)
for i in range(len(ld)):
    print(ld[i][0])