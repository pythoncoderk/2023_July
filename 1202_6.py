from datetime import datetime, timedelta

d1 = datetime(2020, 12, 25)
d2 = datetime(2020, 11, 25)
result = d1 - d2
print(result)
print(result.days)

test = d1 + timedelta()
