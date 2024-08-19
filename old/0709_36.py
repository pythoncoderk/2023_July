t, x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(t)]

# print(t, x, y)
# print(l)

if y == 0:
    print(0)
    exit()

max_l = x
for i in range(t):
    x += l[i][0]
    if y + l[i][1] >= 1:
        y += l[i][1]
        if max_l < x:
            max_l = x
    else:
        if max_l < x:
            max_l = x
        break


print(max_l)
