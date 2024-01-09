import datetime

y, m, d = map(int, input().split())
x = datetime.datetime(y, m, d)
y = x.weekday()

if y == 0:
    z = "月"
elif y == 1:
    z = "火"
elif y == 2:
    z = "水"
elif y == 3:
    z = "木"
elif y == 4:
    z = "金"
elif y == 5:
    z = "土"
elif y == 6:
    z = "日"

print(f"{z}曜日")