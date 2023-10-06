l = list(map(int, input().split()))
for i in range(10):
    if i == 9:
        print(l[i])
    else:
        print(l[i], end=",")