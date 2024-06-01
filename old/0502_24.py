import datetime

n, m, s = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, m, s)
# print(l)

max_time = datetime.timedelta(minutes=m, seconds=s)
# print(max_time)

l2 = [datetime.timedelta(minutes=l[i][0], seconds=l[i][1]) for i in range(n)]
l2.sort()
# print(l2)

total = datetime.timedelta(minutes=0, seconds=0)
count = 0
for i in range(n):
    total += l2[i]
    if total <= max_time:
        count += 1
print(count)