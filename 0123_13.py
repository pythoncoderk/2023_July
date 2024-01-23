n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
# print(l)

point = 0
for i in range(n):

    if len(l[i][0]) != len(l[i][1]):
        pass
    elif l[i][0] == l[i][1]:
        point += 2
    else:
        count_l = []
        for j in range(len(l[i][0])):
            if l[i][0][j] == l[i][1][j]:
                count_l.append(1)
        if sum(count_l)+1 == len(l[i][0]):
            point += 1
print(point)