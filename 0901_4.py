p, q, r = map(int, input().split())
d = {}
for i in range(p):
    x, y = map(int, input().split())
    d[x] = y

d2 = {}
for i in range(q):
    x, y = map(int, input().split())
    d2[x] = y



# print(d)
# print(d2)


for i in range(1, p + 1):
    print(i, d2[d[i]])