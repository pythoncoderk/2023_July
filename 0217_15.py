n, k = map(int, input().split())
l = [list(map(str, input().split())) for i in range(n)]
l2 = [list(map(str, input().split())) for i in range(k)]
for i in range(k):
    l2[i][0] = int(l2[i][0])
# print(n, k)
# print(l)
# print(l2)

for i in range(k):
    l[l2[i][0]-1][0] = l2[i][1]
for i in l:
    print(*i)