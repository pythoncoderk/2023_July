n, k = map(int, input().split())
l = [list(map(str, input().split())) for i in range(n)]
l2 = [int(input()) for i in range(k)]
for i in range(n):
    l[i][0] = int(l[i][0])
d = dict(l)

# print(n, k)
# print(d)
# print(l2)

for i in range(k):
    print(d[l2[i]])