n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

for i in range(n):
    for j in range(len(l[i])):
        if j != 0:
            l[i][j] = int(l[i][j])
# print(n)
# print(l)

count = 0
for i in range(n):
    x = l[i][1] + l[i][2] + l[i][3] + l[i][4] + l[i][5]
    s = l[i][2] + l[i][3]
    lang = l[i][4] + l[i][5]
    if l[i][0] == "s":
        if x >= 350 and s >= 160:
            count += 1
    else:
        if x >= 350 and lang >= 160:
            count += 1
print(count)