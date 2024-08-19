n, k, p = map(int, input().split())
l = [int(input()) for i in range(n)]
l2 = [list(map(str, input().split())) for i in range(k)]

# print(n, k, p)
# print(l)
# print(l2)

l.append(p)

for i in range(k):
    if len(l2[i]) >= 2:
        l2[i][1] = int(l2[i][1])

for i in range(k):
    if l2[i][0] == "join":
        l.append(l2[i][1])
    else:
        l.sort()
        print(l.index(p) + 1)

