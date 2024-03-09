n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)
points = 0
count = 0
for i in range(n):
    if l[i][0] == l[i][1]:
        points += 2
    elif len(l[i][0]) != len(l[i][1]):
        pass
    else:
        for j in range(len(l[i][0])):
            if l[i][0][j] != l[i][1][j]:
                count += 1
        if count == 1:
            points += 1
    count = 0

print(points)