import datetime

n, m, s = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, m, s)
# print(l)
time_change = []
for i in range(n):
    time_change.append(datetime.timedelta(minutes=l[i][0], seconds=l[i][1]))
time_change.sort()
# for i in time_change:
#     print(i)

max_time = datetime.timedelta(minutes=m, seconds=s)
# print(max_time)
total_time = datetime.timedelta(minutes=0, seconds=0)
count = 0
for i in range(n):
    if total_time + time_change[i] <= max_time:
        total_time += time_change[i]
        count += 1
print(count)
