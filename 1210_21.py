import datetime

y, m, d = map(int, input().split())
# print(y, m, d)
count_days = datetime.date(y,m,d)
# print(count_days)
if count_days >= datetime.date(2019,5,1):
    print(f"令和年{m}月{d}日")
elif count_days >= datetime.date(1989,1,8):
    print(f"平成年{m}月{d}日")
elif count_days >= datetime.date(1926,12,25):
    print(f"昭和年{m}月{d}日")
elif count_days >= datetime.date(1912,7,30):
    print(f"大正年{m}月{d}日")
else:
    print(f"明治年{m}月{d}日")