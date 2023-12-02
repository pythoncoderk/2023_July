from datetime import datetime, timedelta

n, m, s = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
print(n, m, s)
print(l)

have_time = datetime.time(minute=m, second=0)
print(have_time)

dj_time = datetime.time(minute=l[0][0], second=l[0][1])

print(dj_time)

