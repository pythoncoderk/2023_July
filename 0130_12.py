import sys

t, x, y = map(int, input().split())
l = [list(map(int, input().split())) for i in range(t)]
# print(t, x, y)
# print(l)
max_l = x

for i in range(t):
    x += l[i][0]
    y += l[i][1]
    if x > max_l:
        max_l = x
    if y <= 0:
        break
    else:
        if x > max_l:
            max_l = x
print(max_l)