n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
# print(n)
# print(l)
l2 = []
for i in range(n):
    x = l[i][0] + l[i][1]
    l2.append(x)
# print(l2)
d = {}
for i in range(n):
    d[l2[i]] = l2.count(l2[i])

y = sorted(d.items(), key=lambda x:x[1])
# print(d)
d_max = max(d.values())
l_final = []
for i in d:
    if d_max == d[i]:
        l_final.append(i)
l_final.sort()
print(l_final[0])