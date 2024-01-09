import datetime

y, m, d = map(int, input().split())

x = datetime.datetime(y, m, d)

if x >= datetime.datetime(2019, 5, 1):
    g = "令和"
elif x >= datetime.datetime(1989, 1, 8) and x <= datetime.datetime(2019, 4, 30):
    g = "平成"
elif x >= datetime.datetime(1926, 12, 25) and x <= datetime.datetime(1989, 1, 7):
    g = "昭和"
elif x >= datetime.datetime(1912, 7, 30) and x <= datetime.datetime(1989, 1, 7):
    g = "大正"
else:
    g = "明治"

print(f"{g}年{m}月{d}日")