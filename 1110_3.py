n = int(input())
l = [list(map(int, input().split())) for i in range(2)]
l2 = list(set(l[0] + l[1]))
l2.sort()
for i in range(len(l2)):
    if i == len(l2)-1:
        print(l2[i])
    else:
        print(l2[i], end=" ")