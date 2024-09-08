l = list(map(int, input().split()))

l2 = []
for i in range(len(l)):
    l2.append(l.count(l[i]))

for i in range(len(l)):
    if l2[i] == 1:
        print(l[i])
        break