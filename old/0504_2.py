n, m = map(int, input().split())
l = [input() for i in range(m)]

# print(n, m)
# print(l)

l.reverse()
# print(l)

ng = l[:n]
ok = l[n:]

# print(ng)
# print(ok)

l2 = []
for i in range(len(ok)):
    if ok[i] not in ng:
        l2.append(ok[i])

l2 = set(l2)
print(len(l2))