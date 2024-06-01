h, w = map(int, input().split())
l = [list(map(int, input().split())) for i in range(h)]

print(h, w)
print(l)

l2 = []
for i in range(h):
    l3 = []
    for j in range(w):
        l3.append(l[j].pop(0))
    l2.append(l3)
print(l2)

l4 = []
for q in range((h * w)//9):
    for i in range(3):
        l5 = []
        for j in range(3):
            l5.append(l2[j].pop(0))