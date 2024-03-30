a, b = map(str, input().split())
l = []
a1 = len(a)
b1 = len(b)
if a1 == b1:
    ab = a1
elif a1 > b1:
    ab = a1
else:
    ab = b1

count = 0
while count <= ab:
    if a != "":
        x1 = a[-1]
        a = a[:-1]
    else:
        x1 = 0

    if b != "":
        y1 = b[-1]
        b = b[:-1]
    else:
        y1 = 0

    z1 = int(x1) + int(y1)
    z1 = str(z1)[-1]
    l.append(z1)
    count += 1

l_f = [l[i] for i in range(ab)]
l_f.reverse()
# print(l_f)

for i in l_f:
    print(i, end="")