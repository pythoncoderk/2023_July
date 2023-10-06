l = list(map(int, input().split()))
for i in range(len(l)):
    if i == len(l) - 1:
        print(l[i])
    else:
        print(l[i], end=",")