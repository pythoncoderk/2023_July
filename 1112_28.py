n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
x, y = map(int, input().split())
l2 = []
for i in range(n):
    if int(l[i][1]) >= x and int(l[i][1]) <= y:
        l2.append(l[i][0])
for i in l2:
    print(i)