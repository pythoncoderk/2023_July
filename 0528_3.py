n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(l)

d = {}
for i in range(n):
    if l[i][0] == "1":
        d[l[i][1]] = l[i][2]
    else:
        print(d[l[i][1]])

