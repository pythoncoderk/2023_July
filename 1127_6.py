from datetime import time

n, m, s = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
print(n, m, s)
print(l)
have_time = time(0,m,s)
print(have_time)
l_times = []
for i in range(n):
    x = time(minute=l[i][0], second=l[i][1])
    l_times.append(x)
for i in range(n):
    a = 0
    b = 0
    c = l_times.pop(b)
    for j in range(n-1):
        if str(c) + str(l_times[j]) <= str(have_time):
            a += 1
            b += 1
print(b)

