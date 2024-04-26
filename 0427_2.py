n = int(input())

l = [list(map(str, input().split())) for i in range(n)]
l2 = [[l[i][0], float(l[i][1])] for i in range(n)]

# print(n)
# print(l2)

ge_max = 0
le_min = 9999.9

for i in range(n):
    if l2[i][0] == "ge":
        if l2[i][1] > ge_max:
            ge_max = l2[i][1]
    else:
        if l2[i][1] < le_min:
            le_min = l2[i][1]

print(ge_max, le_min)