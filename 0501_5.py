at, df, ag = map(int, input().split())
n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
l2 = [[int(l[i][j]) if l[i][j].isdecimal() else l[i][j] for j in range(7)] for i in range(n)]

# print(at, df, ag)
# print(n)
# print(l2)

count = 0
for i in range(n):
    if l2[i][1] <= at <= l2[i][2]:
        if l2[i][3] <= df <= l2[i][4]:
            if l2[i][5] <= ag <= l2[i][6]:
                count += 1
                print(l2[i][0])

if count == 0:
    print("no evolution")