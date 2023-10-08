l = list(map(int, input().split()))

for i in range(9):
    if (i+1) % 3 == 0 and i != 0:
        print(l[i])
    else:
        print(l[i], end=" ")