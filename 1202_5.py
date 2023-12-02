from datetime import datetime, timedelta

n, m, s = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
print(n, m, s)
print(l)

have_time = time(minute=m)
print(have_time)

dj_time = time(minute=l[0][0], second=l[0][1])

test = have_time + time(minute=dj_time.minute, second=dj_time.second)
print(test)

