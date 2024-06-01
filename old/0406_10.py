from datetime import datetime, timedelta

n, m, s = map(int, input().split())

l = [list(map(int, input().split())) for i in range(n)]

# print(n, m, s)
# print(l)
dj_time = timedelta(minutes=m, seconds=s)
# print(dj_time)

sort_time = sorted(l, key=lambda k: (k[0], k[1]))
# print(sort_time)

times = []
for i in range(n):
    x_time = timedelta(hours=0, minutes=sort_time[i][0], seconds=sort_time[i][1])
    times.append(x_time)
# print(times)

total = timedelta(minutes=0, seconds=0)
count = 0
for i in range(n):
    total += times[i]
    if total > dj_time:
        print(count)
        exit()
    else:
        count += 1
print(count)
