n, q = map(int, input().split())
l = list(map(int, input().split()))
l2 = [list(map(int, input().split())) for i in range(q)]

l2 = [[l2[i][0]-1, l2[i][1]-1] for i in range(len(l2))]

print(n, q)
print(l)
print(l2)

x = 0
l3 = []
for i in range(len(l)):
    x += l[i]
    l3.append(x)

print(l3)

for i in range(len(l2)):
    if l2[i][0] >= 1:
        a = l2[i][0] - 1
    else:
        a = 0

    if l2[i][0] - 1 <= -1:
        print(l3[l2[i][1]] - l3[a])
    else:
        print(l3[l2[i][1]])