n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)
l2 = []
for i in range(n):
    if l[i][0] == "make":
        l2.append(l[i])
    elif l[i][0] == "getnum":
        x = int(l[i][1])-1
        print(l2[x][1])
    elif l[i][0] == "getname":
        x = int(l[i][1])-1
        print(l2[x][2])