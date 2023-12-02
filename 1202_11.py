import datetime

n, m, s = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
print(n, m, s)
print(l)
dj_times = []
for i in range(n):
    x = datetime.time(minute=l[i][0], second=l[i][1])
    dj_times.append(x)
dj_times.sort()
fmt = "%H:%M:%S"
print(dj_times)