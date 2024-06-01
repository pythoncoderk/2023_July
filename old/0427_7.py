n, s, p = map(int, input().split())

# print(n, s, p)

l = [i+1 for i in range(n)]

# print(l)

l2 = []
l3 = []
for i in range(n):
    if (i+1) % s == 0:
        l3.append(l[i])
        l2.append(l3)
        l3 = []
    else:
        l3.append(l[i])
l2.append(l3)

# print(l2)

if len(l2) < p:
    if len(l2[p-1]) == 0:
        print("none")
    else:
        print(*l2[p - 1])
else:
    print(*l2[p-1])