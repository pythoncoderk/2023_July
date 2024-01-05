from datetime import timedelta
import sys

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
total_time = timedelta(hours=0, minutes=0)
max_time = timedelta(hours=74,)
for i in range(n):
    td = timedelta(hours=l[i][0], minutes=l[i][1],)
    total_time += td
    if total_time > max_time:
        print("No")
        sys.exit()
print("Yes")


