n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
print(n)
print(l)
l2 = []
for i in range(n):
    l2.append(sum(l[i]))
print(l2)
d = {}
for i in range(n):
    d[l2[i]] = l2.count(l2[i])
print(d)
d_max = max(d.values())
d2 = {}
print(d[d_max])

finals = sorted(d.items(), key=lambda x:x[1])
finals.sort()
print(finals[0][0])