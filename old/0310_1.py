n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
l2 = [[int(l[i][j]) if j == 1 else l[i][j] for j in range(2)] for i in range(n)]
# print(l2)

l3 = [l2[i][1] for i in range(n)]
# print(l3)

min_l = min(l3)
index_l = l3.index(min_l)

# print(min_l)
# print(index_l)

x1 = l3[index_l:]
x2 = l3[:index_l]
x3 = x1 + x2
# print(x3)

for i in range(n):
    for j in range(n):
        if x3[i] == l2[j][1]:
            print(l2[j][0])