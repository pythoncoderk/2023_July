n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])
m = int(input())
l2 = [list(map(str, input().split())) for i in range(m)]
for i in range(m):
    l2[i][1] = int(l2[i][1])

dic1 = dict(l)
dic2 = dict(l2)

# print(dic1)
# print(dic2)
ok = 0
counts = 0
while counts == 0:
    for i in dic1:
        if i in dic2:
            if dic2[i] - dic1[i] >= 0:
                dic2[i] -= dic1[i]
            else:
                counts += 1
                break
        else:
            counts += 1
    if counts == 0:
        ok += 1
print(ok)