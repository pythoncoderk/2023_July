n = int(input())
l = list(map(int, input().split()))
l2 = list(set(l))
l2.sort()
for i in range(len(l2)):
    if i == len(l2)-1:
        print(l2[i])
    else:
        print(l2[i], end=" ")