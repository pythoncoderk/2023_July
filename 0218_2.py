import datetime


time1 = [2, 15, 30]
time2 = [6, 45, 59]
time3 = [23, 1, 19]
time4 = [5, 24, 3]

time1delta = datetime.timedelta(hours=time1[0], minutes=time1[1], seconds=time1[2])
time2delta = datetime.timedelta(hours=time2[0], minutes=time2[1], seconds=time2[2])
print(time1delta + time2delta)

time3delta = datetime.timedelta(hours=time3[0], minutes=time3[1], seconds=time3[2])
time4delta = datetime.timedelta(hours=time4[0], minutes=time4[1], seconds=time4[2])
print(time3delta + time4delta)

