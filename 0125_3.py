n = int(input())
l = list(map(str, input().split()))
m = int(input())
l2 = [list(map(str, input().split())) for i in range(m)]
for i in range(m):
    l2[i][1] = int(l2[i][1])
# print(l)
# print(l2)

l3 = []
for i in range(n):
    x = 0
    for j in range(m):
        if l[i] == l2[j][0]:
            x += l2[j][1]
    l3.append(x)
# print(l3)

d = {l3[k]: l[k] for k in range(n)}
# print(d)

d_sort = sorted(d.items(), key=lambda x:x[0], reverse=True)
d_list = list(d_sort)

for i in d_list:
    print(i[1])