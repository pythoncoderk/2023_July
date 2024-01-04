n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][0] = int(l[i][0])
l2 = []
# print(n)
# print(l)
for i in range(n):
    if l[i][0] == 1:
        l2.append(l[i][1])
        print(*l2)
    elif l[i][0] == 2:
        print(l2.pop())
        print(*l2)


