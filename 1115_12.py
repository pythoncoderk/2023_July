import datetime

t = datetime.datetime.today()

dt_now = datetime.datetime.now()
cc_days = (datetime.datetime(2023,12,31) - datetime.datetime(t.year, t.month, t.day))
print(f"今年はあと{cc_days.days}日")