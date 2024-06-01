t = int(input())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(t)
# print(n)
# print(l)

all_time = [0] * (t + 1)

# print(all_time)

for i in range(n):
    all_time[l[i][0]] += 1
    all_time[l[i][1]] -= 1

# print(all_time)

x = 0
for i in range(t):
    x += all_time[i]
    print(x)