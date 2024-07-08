n, k = map(int, input().split())
l = {input() for i in range(n)}
l2 = [list(map(str, input().split())) for i in range(k)]

# print(n, k)
# print(l)
# print(l2)

for i in range(k):
    if l2[i][0] == "handshake":
        l_set = list(l[::])
        l_set.sort()
        for j in range(len(l)):
            l_set = list(l[::])
            print(l_set[j])
    elif l2[i][0] == "leave":
        l_set = list(l[::])
        l_set.pop(l_set.index(l2[i][1]))
    else:
        l_set = list(l[::])
        l_set.append(l2[i][1])

    l = l_set