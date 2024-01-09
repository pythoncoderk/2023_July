y, m, d = map(int, input().split())

if y % 4 == 0:
    if y % 100 == 0:
        chck_y = 0
    elif y % 400 == 0:
        chck_y = 1
    else:
        chck_y = 1
else:
    chck_y = 0

if m == 4 or m == 6 or m == 9 or m == 11:
    chck_d = 30
elif m == 2:
    if chck_y == 1:
        chck_d = 29
    else:
        chck_d = 28
else:
    chck_d = 31

if d == chck_d:
    d = 1
    m += 1
else:
    d += 1

if m == 13:
    m = 1
    y += 1

print(f"{y} {m} {d}")