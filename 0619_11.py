n, q = map(int, input().split())
l = list(map(int, input().split()))
l2 = [list(map(int, input().split())) for i in range(q)]

# print(n, q)
# print(l)
# print(l2)

x = 0
for i in range(n):
    l[i] += x
    x = l[i]
l.insert(0, 0)

# print(l)

for i in range(q):
    print(l[l2[i][1]] - l[l2[i][0] - 1])