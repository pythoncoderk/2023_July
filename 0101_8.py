n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)
points = 0
for i in range(n):
    if l[i][0] == l[i][1]:
        points += 2
    elif len(l[i][0]) == len(l[i][1]):
        x = list(l[i][0])
        y = list(l[i][1])
        l2 = []
        for j in range(len(x)):
            if x[j] == y[j]:
                l2.append(1)
            else:
                l2.append(0)
        if sum(l2) == len(x)-1:
            points += 1

print(points)