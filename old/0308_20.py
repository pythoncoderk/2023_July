n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
d = {l[k][0]: int(l[k][1]) for k in range(n)}
m_l = list(map(str, input().split()))
# print(n)
# print(d)
# print(m_l)

time_chk = d[m_l[0]]
time_h = int(m_l[1][:2])
# print(time_chk)
# print(time_h)

for i in range(n):
    diff = int(l[i][1]) - time_chk
    out_time = diff + time_h
    if out_time < 0:
        out_time += 24
    elif out_time >= 24:
        out_time -= 24
    print(f"{str(out_time).zfill(2)}{m_l[1][-3:]}")
