n, q = map(int, input().split())
l = list(map(int, input().split()))
l2 = [list(map(int, input().split())) for i in range(q)]

# print(n, q)
# print(l)
# print(l2)

l3 = []
x = 0
for i in range(n):
    x += l[i]
    l3.append(x)

l3.insert(0, 0)


# print(l3)

for i in range(q):
    print(l3[l2[i][1]] - l3[l2[i][0] - 1])