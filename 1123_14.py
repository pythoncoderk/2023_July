y, m, d = map(int, input().split())
a, b = map(int, input().split())
# print(f"{y} {m} {d} 基準日")
y2 = y
while y2 % 4 != 1:
    y2 += 1
# print(f"{y2} {a} {b} 開催日")
to_y = y
to_m = m
to_d = d
# print(f"{to_y} {to_m} {to_d} カウント日")
counts = 0
while y2 != to_y or a != to_m or b != to_d:
    to_d += 1
    if to_m % 2 == 0:
        if to_d == 16:
            to_d = 1
            to_m += 1
            if to_m == 14:
                to_m = 1
                to_y += 1
                counts += 1
            else:
                counts += 1
        else:
            counts += 1
    else:
        if to_d == 14:
            to_d = 1
            to_m += 1
            if to_m == 14:
                to_m = 1
                to_y += 1
                counts += 1
            else:
                counts += 1
        else:
            counts += 1
print(counts)