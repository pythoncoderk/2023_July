l = list(map(str, input().split()))
l2 = []

# print(l)

for i in range(len(l)):
    if l[i] in l2:
        print("already_been")

    else:
        print(l[i])
        l2.append(l[i])