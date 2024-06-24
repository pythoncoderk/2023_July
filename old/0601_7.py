n, q = map(int, input().split())
l = list(map(int, input().split()))
l2 = [list(map(int, input().split())) for i in range(q)]

x = 0
l3 = []
for i in range(n + 1):
    if i == 0:
        l3.append(0)
    else:
        x += l[i - 1]
        l3.append(x)

# print(n, q)
# print(l)
# print(l2)
# print(l3)

for i in range(q):
    print(l3[l2[i][1]] - l3[l2[i][0] - 1])


