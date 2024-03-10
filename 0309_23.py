n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
l2 = [[int(l[i][j]) if j == 1 else l[i][j] for j in range(2)] for i in range(n)]

# print(l2)

min_l = l2[0][1]
index_l = l2[0]
for i in range(n):
    if min_l > l2[i][1]:
        min_l = l2[i][1]
        index_l = l2.index(l2[i])

# print(min_l)
# print(index_l)

l3 = [l2[i][0] for i in range(n)]
# print(l3)

x1 = l3[index_l:]
x2 = l3[:index_l]
x3 = x1 + x2
# print(x3)

for i in x3:
    print(i)

