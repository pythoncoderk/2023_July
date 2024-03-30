n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

for i in range(n):
    for j in range(6):
        if j != 0:
            l[i][j] = int(l[i][j])

# print(n)
# print(l)

count = 0
for i in range(n):
    if l[i][1] + l[i][2] + l[i][3] + l[i][4] + l[i][5] >= 350:
        if l[i][0] == "s":
            if l[i][2] + l[i][3] >= 160:
                count += 1
        else:
            if l[i][4] + l[i][5] >= 160:
                count += 1
print(count)


