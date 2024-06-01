n, q = map(int, input().split())
l = list(map(int, input().split()))
l2 = [list(map(int, input().split())) for i in range(q)]

l_count = [[l2[i][0]-1, l2[i][1]-1] for i in range(q)]

print(n, q)
print(l)
print(l2)
print(l_count)

l3 = [l[0]]
x = l[0]
for i in range(len(l)-1):
    x += l[i+1]
    l3.append(x)

print(l3)

for i in range(len(l2)):
    if l_count[i][0] - 1 < 0:
        a = 0
    else:
        a = l_count[i][0] - 1

    if l_count[i][1] - 1 < 0:
        b = 0
    else:
        b = l_count[i][1] - 1

    print(l3[b] - l3[a])

