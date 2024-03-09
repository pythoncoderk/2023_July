import math

m = int(input())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(m)
# print(n)
# print(l)
time_l = l[0][0]
total = 0
count = 0
while l:
    if l[0][0] == time_l:
        total += l[0][2]
        del l[0]
    else:
        time_l = l[0][0]
        count += math.ceil(total / m)
        total = 0
count += math.ceil(total / m)
print(count)