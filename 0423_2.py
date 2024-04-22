n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)

total = 0
for i in range(n):
    if len(l[i][0]) == len(l[i][1]):
        count = 0
        for j in range(len(l[i][0])):
            if l[i][0][j] == l[i][1][j]:
                count += 1
        if len(l[i][0]) == count:
            total += 2
        elif len(l[i][0])-1 == count or len(l[i][0])+1 == count:
            total += 1
print(total)

