n, k = map(int, input().split())
l = [list(map(str, input().split())) for i in range(n)]
l2 = [input() for i in range(k)]

# print(n, k)
# print(l)
# print(l2)

for i in range(k):
    for j in range(n):
        if l2[i] == l[j][0]:
            print(l[j][1])
            break


