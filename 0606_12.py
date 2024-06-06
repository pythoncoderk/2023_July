import math

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    l[i][0] = str(l[i][0])

# print(n)
# print(l)

point = 0
for i in range(n):
    if "3" in l[i][0]:
        point += math.floor(l[i][1] * 0.03)
    elif "5" in l[i][0]:
        point += math.floor(l[i][1] * 0.05)
    else:
        point += math.floor(l[i][1] * 0.01)
print(point)