n, k = map(int, input().split())
l = [input() for i in range(n)]
l2 = [list(map(str, input().split())) for i in range(k)]

# print(n, k)
# print(l)
# print(l2)


for i in range(k):
    if l2[i][0] == "handshake":
        l3 = l[::]
        l3.sort()
        for j in range(len(l3)):
            print(l3[j])
    elif l2[i][0] == "join":
        l.append(l2[i][1])
    elif l2[i][0] == "leave":
        for q in range(len(l)):
            if l[q] == l2[i][1]:
                l.pop(q)
                break