n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
m = int(input())
l2 = [list(map(str, input().split())) for i in range(m)]
l3 = [l2[i][0] for i in range(m)]

for i in range(n):
    l[i][1] = int(l[i][1])

for i in range(m):
    l2[i][1] = int(l2[i][1])

# print(n)
# print(l)
# print(m)
# print(l2)

d = dict(l)
d2 = dict(l2)

# print(d)
# print(d2)

x = 0
count = 0
while True:
    if l[x][0] not in l3:
        break
    if d2[l[x][0]] >= l[x][1]:
        d2[l[x][0]] -= l[x][1]
    else:
        break
    x += 1
    if x >= n:
        count += 1
        x = 0

print(count)


