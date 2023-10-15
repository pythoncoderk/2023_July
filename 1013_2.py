a, b, c = map(int, input().split())
points = list(map(float, input().split()))
l3 = []
for i in range(b):
    l = list(map(int, input().split()))
    l2 = []
    for j in range(a):
        l2.append(l[j])
l3.append(l2)

l4 = []
for i in l3:
    l4.append(sum(i))

l5 = []
for i in l4:
    l5.append(round(i))

l5.sort()
x = -1
for i in range(c):
    print(l5[x])
    x -= 1
