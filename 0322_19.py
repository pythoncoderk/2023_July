t, x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(t)]

# print(t, x, y)
# print(l)

max_x = x

if y <= 0:
    print(0)
    exit()

for i in range(t):
    x += l[i][0]
    y += l[i][1]
    if y <= 0:
        break
    else:
        if max_x < x:
            max_x = x
print(max_x)