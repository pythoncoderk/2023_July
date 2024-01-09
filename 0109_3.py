y, m = map(int, input().split())

if y % 4 == 0:
    if y % 400 == 0:
        check_y = 1
    elif y % 100 == 0:
        check_y = 0
    else:
        check_y = 1
else:
    check_y = 0

if m == 4 or m == 6 or m == 9 or m == 11:
    check_d = 30
elif m == 2:
    if check_y == 1:
        check_d = 29
    else:
        check_d = 28
else:
    check_d = 31

print(check_d)

