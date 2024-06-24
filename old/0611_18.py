h, w = map(int, input().split())
l = [list(map(int, input().split())) for i in range(h)]
q = int(input())
l2 = [list(map(int, input().split())) for i in range(q)]

print(h, w)
print(l)
print(q)
print(l2)

l3 = []
for i in range(h):
    l4 = []
    x = 0
    for j in range(w):
        x += l[i][j]
        l4.append(x)
    l3.append(l4)

print(l3)

