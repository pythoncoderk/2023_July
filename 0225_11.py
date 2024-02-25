n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

up_l = []
down_l = []
up = 0
down = 0
for i in range(n-1):
    if l[i+1] - l[i] < 0:
        up += 1
        up_l.append(up)
        down = 0
    else:
        down += 1
        down_l.append(down)
        up = 0

final_up = 9999
final_down = 9999
if up_l == []:
    final_up = 0
if down_l == []:
    final_down = 0

if final_up == 9999:
    final_up = max(up_l)

if final_down == 9999:
    final_down = max(down_l)

print(final_up, final_down)
