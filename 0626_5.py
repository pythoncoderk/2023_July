l = list(map(str, input().split()))
l2 = []

for i in range(len(l)):
    if l[i] not in l2:
        l2.append(l[i])
        print(l[i])
    else:
        print("already_been")