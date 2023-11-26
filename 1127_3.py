n = int(input())
l = [int(input()) for i in range(n)]
# print(n)
# print(l)
c_down = 0
c_up = 0
l_down = []
l_up = []
for i in range(n-1):
    if l[i] - l[i+1] > 0:
        c_down += 1
        l_down.append(c_down)
        c_up = 0
    else:
        c_up += 1
        l_up.append(c_up)
        c_down = 0
if l_down == []:
    max_l_down = 0
else:
    max_l_down = max(l_down)
if l_up == []:
    max_l_up = 0
else:
    max_l_up = max(l_up)
print(f"{max_l_down} {max_l_up}")