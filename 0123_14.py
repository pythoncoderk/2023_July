n = int(input())
l1 = [list(map(str, input().split())) for i in range(n)]
l2 = list(map(str, input().split()))
for i in range(n):
    l1[i][1] = int(l1[i][1])
# print(l1)
# print(l2)

chk = l2[1].index(":")
# print(chk)
time_h = int(l2[1][:chk])
time_m = int(l2[1][chk+1:])

d = {l1[k][0]:l1[k][1] for k in range(n)}
# print(d)

diff_time = d[l2[0]]
if time_h - diff_time <= 0:
    time_h = time_h - diff_time + 24
else:
    time_h -= diff_time
# print(time_h)
# print(time_m)

for i in range(n):
    if time_h + int(l1[i][1]) >= 24:
        x = str(time_h + int(l1[i][1]) - 24)
        print(f"{x.zfill(2)}:{str(time_m).zfill(2)}")
    elif time_h + int(l1[i][1]) < 0:
        x = str(time_h + int(l1[i][1]) + 24)
        print(f"{x.zfill(2)}:{str(time_m).zfill(2)}")
    else:
        x = str(time_h + int(l1[i][1]))
        print(f"{x.zfill(2)}:{str(time_m).zfill(2)}")