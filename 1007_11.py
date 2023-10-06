n = list(map(int, input()))
n.reverse()
l = []
for i in range(len(n)):
    if i != 0 and (i+1) % 3 == 0:
        l.append(n[i])
        l.append(",")
    else:
        l.append(n[i])
l.reverse()
for i in range(len(l)):
    if i == 0:
        if l[i] == ",":
            pass
        else:
            print(l[i], end="")
    else:
        print(l[i], end="")