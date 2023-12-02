import datetime
from datetime import time

n, m, s = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
print(n, m, s)
print(l)
l_dj_time = []
for i in range(n):
    dj_time = time(minute=l[i][0], second=l[i][1])
    l_dj_time.append(dj_time)
l_dj_time.sort()
print(l_dj_time)
total_time = time(hour=0,minute=0,second=0)
have_time = time(minute=0)
print(have_time)
# for i in range(n):
#     if have_time > total_time:
#         total_time += l_dj_time[i]

result_time = datetime.combine(datetime.min, total_time) + timedelta(minutes=have_time.minute)

# 結果を表示
print(result_time.time())