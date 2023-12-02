m, d = map(int, input().split())
y1, m1, d1 = map(int, input().split())
# print(m, d)
# print(y1, m1, d1)
final_y = y1
final_m = m1
final_d = 1
if d < d1 + 1:
    m1 += 1
    if m < m1:
        final_y = y1 + 1
        final_m = 1
    else:
        final_m = m1
else:
    final_d = d1 + 1

print(f"{final_y} {final_m} {final_d}")