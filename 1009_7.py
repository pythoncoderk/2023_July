x, y = map(int, input().split())
l = list(map(int, input().split()))
l2 = list(map(int, input().split()))
z = 0
for i in range(y):
    for j in range(l2[i]):
        if j+1 == l2[i]:
            print(l[z])
            z += 1
        else:
            print(l[z],end=" ")
            z += 1

