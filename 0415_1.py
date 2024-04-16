h, w = map(int, input().split())
l = [list(map(int, input().split())) for i in range(h)]

print(h, w)
print(l)

l2 = []
for i in range(h):
    l4 = []
    for j in range(w//3):
        l3 = []
        for q in range(3):
            l3.append(l[0].pop(0))
        l4.append(l3)
        if l[0] == []:
            del l[0]
    l2.append(l4)
print(l2)