import math

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
# print(l)

l_0 = []
l_1 = []
l_2 = []
l_3 = []

for i in range(n):
    if l[i][0] == 0:
        l_0.append(l[i][1])
    elif l[i][0] == 1:
        l_1.append(l[i][1])
    elif l[i][0] == 2:
        l_2.append(l[i][1])
    elif l[i][0] == 3:
        l_3.append(l[i][1])

max_0 = math.floor(sum(l_0)/100)
max_1 = math.floor(sum(l_1)/100)
max_2 = math.floor(sum(l_2)/100)
max_3 = math.floor(sum(l_3)/100)

print(max_0 * 5 + max_1 * 3 + max_2 * 2 + max_3 * 1)
