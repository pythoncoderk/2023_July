n, m = map(int, input().split())
h, w = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

print(n, m)
print(h, w)
print(l)

space = []
for i in range(h):
    in_space = []
    for j in range(w):
        in_space.append(".")
    space.append(in_space)
print(space)

for i in range(n):
    space[0][3] = l[0][4]
    space[0][4] = 