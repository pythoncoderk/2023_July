h, w = map(int, input().split())
l = [list(map(int, input().split())) for i in range(h)]

print(h, w)
print(l)

for i in range(3):
    l2 = []
    for j in range(3):
        x = l[i].pop(0)
        l2.append(x)