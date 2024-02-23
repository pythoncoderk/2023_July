h, w = map(int, input().split())
l = [list(map(int, input().split())) for i in range(h)]

# print(h, w)
# print(l)

l3 = []
l2 = []
for k in range(w//3):
    for i in range(h):
        for j in range(3):
            l2.append(l[i].pop(0))
    l3.append(l2)
    l2 = []

# print(l3)
l4 = []
for i in range(len(l3)):
    l4 += l3[i]
# print(l4)

l5 = []
for i in range(len(l4)//9):
    total_3 = 0
    for j in range(9):
        total_3 += l4.pop(0)
    l5.append(total_3//9)
# print(l5)

h_f = []
w_f = []

for i in range(len(l5)):
    if i % 2 == 0:
        h_f.append(l5[i])

for i in range(len(l5)):
    if i % 2 != 0:
        w_f.append(l5[i])

print(*h_f)
print(*w_f)