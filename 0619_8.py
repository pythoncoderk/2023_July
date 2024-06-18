p = [list(map(int, input().split())) for i in range(2)]
e = list(map(int, input().split()))
f = list(map(int, input().split()))

for i in range(2):
    for j in range(2):
        p[i][j] -= 1

# print(p)
# print(e)
# print(f)

farst = 0
if e[p[0][0]] < e[p[0][1]]:
    farst = p[0][0]
else:
    farst = p[0][1]

seconds = 0
if e[p[1][0]] < e[p[1][1]]:
    seconds = p[1][0]
else:
    seconds = p[1][1]

l = [farst, seconds]
l.sort()

if f[0] < f[1]:
    print(l[0] + 1)
    print(l[1] + 1)
else:
    print(l[1] + 1)
    print(l[0] + 1)

