n = int(input())
l = [int(input()) for i in range(n)]
m = int(input())
l2 = [list(map(int, input().split())) for i in range(m)]

# print(n)
# print(l)
# print(m)
# print(l2)

l3 = [0] * n
# print(l3)

for i in range(m):
    for j in range(l2[i][0]-1, l2[i][1]):
        if l2[i][2] + l3[j] <= l[j]:
            l3[j] += l2[i][2]
        else:
            l3[j] = l[j]
for i in l3:
    print(i)