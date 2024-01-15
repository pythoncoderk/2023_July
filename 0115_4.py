import datetime

n, m, s = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
l.sort()

dj_time = datetime.timedelta(minutes=m, seconds=s)
total_time = datetime.timedelta(minutes=0, seconds=0)

time_count = 0
for i in range(n):
    this_time = datetime.timedelta(minutes=l[i][0], seconds=l[i][1])
    total_time += this_time
    if total_time <= dj_time:
        time_count += 1

print(time_count)