p1, p2 = map(int, input().split())
p3, p4 = map(int, input().split())
e = list(map(int, input().split()))
f = list(map(int, input().split()))

# print(p1, p2)
# print(p3, p4)
# print(e)
# print(f)
second_1 = []
win1 = 0
win2 = 0
if e[p1-1] < e[p2-1]:
    second_1.append(p1)
    win1 = p1
else:
    second_1.append(p2)
    win1 = p2

if e[p3-1] < e[p4-1]:
    second_1.append(p3)
    win2 = p3
else:
    second_1.append(p4)
    win2 = p4
# print(second_1)
w = []
if win1 < win2:
    w.append(win1)
    w.append(win2)
else:
    w.append(win2)
    w.append(win1)

# print(f)
if f[0] < f[1]:
    print(w[0])
    print(w[1])
else:
    print(w[1])
    print(w[0])