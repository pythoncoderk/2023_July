n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

for i in range(n):
    for j in range(5):
        l[i][j+1] = int(l[i][j+1])
# print(l)
OK = 0
for i in range(n):
    total1 = 0
    total2 = 0
    for j in range(1, 6):
        total1 += l[i][j]
    if l[i][0] == "s":
        total2 = l[i][2] + l[i][3]
    else:
        total2 = l[i][4] + l[i][5]
    if total1 >= 350 and total2 >= 160:
        OK += 1
print(OK)


