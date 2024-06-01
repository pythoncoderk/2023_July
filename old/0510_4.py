d = int(input())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(d)
# print(n)
# print(l)

for i in range(n):
    l[i][0] -= 1

# print(l)

all_day = [0] * (d + 1)

# print(all_day)

for i in range(n):
    all_day[l[i][0]] += 1
    all_day[l[i][1]] -= 1

# print(all_day)

x = 0
for i in range(len(all_day)-1):
    x += all_day[i]
    print(x)
