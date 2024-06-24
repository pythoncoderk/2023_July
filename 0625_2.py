n, s, p = map(int, input().split())

# print(n, s, p)

l = [i for i in range(1, n + 1)]

# print(l)

l2 = []
while l:
    l3 = []
    for i in range(s):
        if l:
            l3.append(l.pop(0))
        else:
            break

    l2.append(l3)

if len(l2) < p:
    print("none")
else:
    print(*l2[p - 1])