n, k, f = map(int, input().split())
l = [int(input()) for i in range(k)]
l = l[f:]
l_f = []
l_f.append(l.pop(0))
while len(l) != 0:
    if l[0] in l_f:
        l.pop(0)
    else:
        l_f.append(l.pop(0))
for i in l_f:
    print(i)