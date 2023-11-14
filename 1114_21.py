n, m = map(int, input().split())
a, b = map(int, input().split())
l = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = [1, 2, 3, 4]
l4 = list(zip(l3, l))
l5 = []

if l[n-1] < l[m-1]:
    l5.append(l4[n-1])
else:
    l5.append(l4[m-1])

if l[a-1] < l[b-1]:
    l5.append(l4[a-1])
else:
    l5.append(l4[b-1])

l5.sort()
l5 = [*l5]
l5[0] = [*l5[0]]
l5[1] = [*l5[1]]

l5[0][1] = l2[0]
l5[1][1] = l2[1]

if l5[0][1] < l5[1][1]:
    print(l5[0][0])
    print(l5[1][0])
else:
    print(l5[1][0])
    print(l5[0][0])