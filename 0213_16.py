n, m = map(int, input().split())
l = [list(map(str, input().split())) for i in range(m)]
for i in range(m):
    for j in range(m):
        if j == 0:
            l[i][j] = int(l[i][j])
# print(n, m)
# print(l)

l2 = [i+1 for i in range(n)]
# print(l2)
final = []
for i in range(n):
    count = []
    for j in range(m):
        if l2[i] % l[j][0] == 0:
            count.append(l[j][1])
    if count == []:
        count.append(l2[i])
    final.append(count)
for i in range(n):
    print(*final[i])