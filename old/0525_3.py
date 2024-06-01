n = int(input())

l = [int(input()) for i in range(n)]

# print(n)
# print(l)

up = 0
up_l = []
for i in range(n-1):
    if l[i] < l[i+1]:
        up += 1
        up_l.append(up)
    else:
        up = 0

down = 0
down_l = []
for i in range(n-1):
    if l[i] > l[i+1]:
        down += 1
        down_l.append(down)
    else:
        down = 0

f_down = 0
if len(down_l) == 0:
    f_down = 0
else:
    f_down = max(down_l)


f_up = 0
if len(up_l) == 0:
    f_up = 0
else:
    f_up = max(up_l)

print(f_down, f_up)