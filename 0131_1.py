n, m = map(int, input().split())
h, w = map(int, input().split())

l = [list(map(int, input().split())) for i in range(n)]

# print(n, m)
# print(h, w)
# print(l)

l2 = [["." for j in range(w)] for i in range(h)]
# print(l2)
total = []
for i in range(n):
    for k in range(2):
        if k == 1 and l[i][0] == l[i][1]:
            break
        for j in range(l[i][2], l[i][3]+1):
            total.append(l2[l[i][k]-1][j-1])
            l2[l[i][k]-1][j-1] = l[i][4]
# print(l2)
for i in range(m):
    print(total.count(i+1))

for i in range(h):
    for j in range(len(l2[i])):
        print(l2[i][j], end="")
    print()