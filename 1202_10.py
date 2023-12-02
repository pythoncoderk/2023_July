from datetime import datetime

s1 = "9:00:00"
s2 = "20:00:00"
fmt = "%H:%M:%S"

tdelta = datetime.strptime(s2, fmt) - datetime.strptime(s1, fmt)

print(tdelta)