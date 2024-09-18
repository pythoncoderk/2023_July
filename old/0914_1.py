l = list(map(int, input().split()))

l2 = []
for i in l:
    l2.append(l.count(i))

chk = True
for i in range(len(l)):
    if l2[i] == 1:
        print(l[i])
        chk = False
        break

if chk:
    print(l[0])
