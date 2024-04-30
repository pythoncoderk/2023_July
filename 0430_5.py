t, x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(t)]

# print(t, x, y)
# print(l)

max_y = x
for i in range(t):
    x += l[i][0]
    y += l[i][1]
    if max_y < x:
        max_y = x
    if y <= 0:
        print(max_y)
        exit()
print(max_y)







