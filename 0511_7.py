l = list(map(int, input().split()))

# print(l)

l2 = []
for i in range(len(l)):
    l2.append(l.count(l[i]))

# print(l2)

if max(l2) == 3:
    print(l[0])
elif max(l2) == 2:
    for i in range(3):
        if l2[i] == 1:
            print(l[i])
            break
elif max(l2) == 1:
    print(0)