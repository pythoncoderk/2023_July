from datetime import datetime
import datetime
n, m, s = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
l.sort()

print(n, m, s)
print(l)

def time_count(time_m, time_s):
    if time_s >= 60:
        time_s = 0
        time_m += 1
        return time_m, time_s
    else:
        return time_m, time_s

total_time_count = 0
total_time = [0, 0]
for i in range(n):
    total_time = total_time[0] + l[0]
    total_time = total_time[1] + l[1]
    print(total_time)