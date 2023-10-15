n = int(input())
l = list(map(int, input().split()))
l2 = list(set(l))
for i in range(len(l2)):
    if i+1 == len(l2):
        print(l2[i])
    else:
        print(l2[i], end=" ")