import math

m = int(input())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
l.append([0,0,0])

# print(l)

time_l = l[0][0]
count_p = 0
count_w = 0
for i in range(n+1):
    if l[i][0] == time_l:
        count_p += l[i][2]
    else:
        count_w += math.ceil(count_p / m)
        count_p = l[i][2]
        time_l = l[i][0]
print(count_w)