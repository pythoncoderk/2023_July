m, n = map(int, input().split())
l = [list(map(int, input().split())) for i in range(m)]

# print(l)
chk_l_f = []
chk_day_f = []
for i in range(m - n + 1):
    chk_l = []
    chk_day = []
    for j in range(i, n + i):
        chk_l.append(l[j][0])
        chk_day.append(l[j][1])
    chk_l_f.append(chk_l)
    chk_day_f.append(sum(chk_day))
# print(chk_day_f)
# print(chk_l_f)

min_l = chk_day_f.index(min(chk_day_f))
# print(min_l)
final_row = min(chk_l_f[min_l])
final_hi = max(chk_l_f[min_l])
print(final_row, final_hi)
