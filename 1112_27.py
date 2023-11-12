n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
m = int(input())
l2 = []

for i in range(n):
    if int(l[i][1]) >= m:
        l2.append(l[i][0])
for i in l2:
    print(i)