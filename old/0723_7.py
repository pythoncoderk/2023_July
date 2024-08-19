a, b = map(int, input().split())

l = []
if a == 1:
    l.append(1)
elif a == 2:
    l.append(2)
elif a == 4:
    l.append(4)
elif a == 3:
    l.append(1)
    l.append(2)
elif a == 0:
    l.append(0)
elif a == 5:
    l.append(1)
    l.append(4)
elif a == 6:
    l.append(2)
    l.append(4)
else:
    l.append(1)
    l.append(2)
    l.append(4)

if b == 1:
    l.append(1)
elif b == 2:
    l.append(2)
elif b == 4:
    l.append(4)
elif b == 3:
    l.append(1)
    l.append(2)
elif b == 0:
    l.append(0)
elif b == 5:
    l.append(1)
    l.append(4)
elif b == 6:
    l.append(2)
    l.append(4)
else:
    l.append(1)
    l.append(2)
    l.append(4)

l_s = set(l)
print(sum(l_s))