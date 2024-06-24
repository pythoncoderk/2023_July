import math

m = int(input())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(m)
# print(n)
# print(l)

now_time = l[0][0]
total = 0
count = 0
for i in range(n):
    if now_time == l[i][0]:
        count += l[i][2]
    else:
        now_time = l[i][0]
        total += math.ceil(count / m)
        count = l[i][2]
total += math.ceil(count / m)
print(total)