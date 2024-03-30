import datetime

k = datetime.timedelta(minutes=int(input()))

t = datetime.timedelta(hours=21, minutes=0)

print(str(t + k)[:-3])

