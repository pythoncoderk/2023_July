y, m, d = map(int, input().split())
y_check = 0

if y % 4 == 0:
    if y % 400 == 0:
        y_check += 1
    elif y % 100 == 0:
        pass
    else:
        y_check += 1
last_day = 0
if y_check == 1 and m == 2:
    last_day = 29
elif m == 2:
    last_day = 28
elif (m == 4 or
      m == 6 or
      m == 9 or
      m == 11):
    last_day = 30
else:
    last_day = 31
# print(last_day)

if m == 12:
    if d == last_day:
        y += 1
        m = 1
        d = 1
    else:
        d += 1
elif m == 2 and y_check == 1:
    if d == last_day:
        m = 3
        d = 1
    else:
        d += 1
elif (m == 4 or
      m == 6 or
      m == 9 or
      m == 11):
    if last_day == d:
        m += 1
        d = 1
    else:
        d += 1
else:
    if last_day == d:
        m += 1
        d = 1
    else:
        d += 1
print(y, m, d)