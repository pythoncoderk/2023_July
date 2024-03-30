n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
m = int(input())
l2 = [list(map(str, input().split())) for i in range(m)]
l3 = [l2[i][0] for i in range(m)]

for i in range(n):
    l[i][1] = int(l[i][1])
for i in range(m):
    l2[i][1] = int(l2[i][1])

d1 = {l[k][0]: l[k][1] for k in range(n)}
d2 = {l2[k][0]: l2[k][1] for k in range(m)}

loop_chk = True

for i in range(n):
    if l[i][0] not in l3:
        loop_chk = False

# print(d1)
# print(d2)
count = 0
while loop_chk:
    for i in range(n):
        if d2[l[i][0]] - l[i][1] >= 0:
            d2[l[i][0]] -= l[i][1]
        else:
            print(count)
            exit()
    count += 1
print(count)
