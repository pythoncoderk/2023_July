a, d, ag = map(int, input().split())
n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])
    l[i][2] = int(l[i][2])
    l[i][3] = int(l[i][3])
    l[i][4] = int(l[i][4])
    l[i][5] = int(l[i][5])
    l[i][6] = int(l[i][6])
counts = 0
for i in range(n):
    if (a >= l[i][1] and a <= l[i][2]) and (d >= l[i][3] and d <= l[i][4]) and (ag >= l[i][5] and ag <= l[i][6]):
        print(l[i][0])
        counts += 1
if counts == 0:
    print("no evolution")