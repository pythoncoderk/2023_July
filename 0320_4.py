n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

for i in range(n):
    if l[i][0] == "change_num":
        l[i][1] = int(l[i][1])
        l[i][2] = int(l[i][2])
    else:
        l[i][1] = int(l[i][1])
# print(n)
# print(l)

l_final = []
for i in range(n):
    if l[i][0] == "make":
        l_final.append([l[i][1], l[i][2]])
    elif l[i][0] == "getnum":
        print(l_final[l[i][1]-1][0])
    elif l[i][0] == "getname":
        print(l_final[l[i][1]-1][1])
    elif l[i][0] == "change_num":
        l_final[l[i][1]-1][0] = l[i][2]
    elif l[i][0] == "change_name":
        l_final[l[i][1]-1][1] = l[i][2]