y, m = map(int, input().split())
y_counts = 0
if y % 4 == 0:
    if y % 400 == 0:
        y_counts += 1
    elif y % 100 == 0:
        pass
    else:
        y_counts += 1
counts_days = 0
if y_counts == 1 and m == 2:
    counts_days =29
elif m == 2:
    counts_days =28
elif m == 4 or m == 6 or m == 9 or m == 11:
    counts_days = 30
else:
    counts_days = 31
print(counts_days)
