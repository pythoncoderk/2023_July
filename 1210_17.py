n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])
k1, k2 = map(int, input().split())
l2 = []
# print(n)
# print(l)
# print(k1, k2)

for i in range(n):
    if l[i][1] >= k1 and l[i][1] <= k2:
        l2.append(l[i][0])
for i in l2:
    print(i)