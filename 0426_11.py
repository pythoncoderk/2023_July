n, s, p = map(int, input().split())

# print(n, s, p)

l = [i for i in range(1, n+1)]

# print(l)

x = 0
l2 = []
l3 = []
while l:
    z = l.pop(0)
    if len(l2) != s:
        l2.append(z)
        x += 1
    else:
        l3.append(l2)
        l2 = []
        l2.append(z)
        x = 0
l3.append(l2)

if len(l3) <= p:
    print("none")
else:
    print(*l3[p-1])