n = int(input())
l = [int(input()) for i in range(n)]
m = int(input())
l2 = [list(map(int, input().split())) for i in range(m)]
l3 = [[l2[i][0]-1, l2[i][1]-1, l2[i][2]] for i in range(m)]

# print(n)
# print(l)
# print(m)
# print(l2)
# print(l3)

l4 = [0] * n
# print(l4)

for i in range(m):
    for j in range(l3[i][0], l3[i][1]+1):
        if l[j] >= l3[i][2] + l4[j]:
            l4[j] += l3[i][2]
        else:
            l4[j] = l[j]
for i in l4:
    print(i)
