s, t = map(str, input().split())
s2 = s[::]
s2 = list(s2)

l = []
x = 1
y = 0
xx = ""
while len(s2) != 0:
    xx += s2.pop(0)
    if x > y:
        y += 1
    else:
        if x >= len(s):
            break
        else:
            l.append(list(xx))
            xx = ""
            x += 1
l.append(list(xx))

print(l)

for i in range(len(l[0])):
    l2 = []
    for j in range(len(l)):
        l2.append(l[i])
