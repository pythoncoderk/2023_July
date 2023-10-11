x, y = map(int, input().split())
l = []
for i in range(x):
    l.append(list(input().split()))
l2 = []
for i in range(y):
    l2.append(input())

l3 = []
for i in range(x):
    l3.append(l[i][0])

l4 = []
for i in range(x):
    l4.append(l[i][1])

for i in range(y):
    if l2[i] in l3:
        print(l[l3.index(l2[i])][1])
    else:
        print(-1)




