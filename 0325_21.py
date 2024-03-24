l = [list(map(int, input().split())) for i in range(2)]
# print(l)

x = l[0][2] / (l[0][0] * l[0][1])
y = l[1][2] / (l[1][0] * l[1][1])

if x == y:
    print("DRAW")
elif x < y:
    print(*l[0])
else:
    print(*l[1])