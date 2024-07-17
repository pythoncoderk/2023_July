n, k = map(int, input().split())
l = [list(map(str, input().split())) for i in range(n)]
l2 = [int(input()) for i in range(k)]

d = {int(l[k][0]): l[k][1] for k in range(n)}



# print(n, k)
# print(d)
# print(l2)

for i in range(k):
    print(d[l2[i]])