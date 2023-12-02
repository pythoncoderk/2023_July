import datetime
from datetime import datetime
import numpy as np

n, m, s = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
arr1 = np.array(l)
print(n,m,s)
print(arr1)
x = np.sort(arr1, axis=0)
print(x)
dj_time = []
for i in range(n):
    change_times = datetime.time(minute=x[i][0], second=x[i][1])
    dj_time.append(str(change_times))
print(dj_time)
fmt = "%H:%M:%S"
final_counts = 0
have_times = str(datetime.time(minute=m))
print(have_times)
for i in range(n):
    if datetime.strptime(have_times, fmt) > datetime.strptime(dj_time, fmt):
        print("OK")
