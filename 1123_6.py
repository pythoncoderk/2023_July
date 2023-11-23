import math

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
total_points = 0
for i in range(n):
    if "3" in str(l[i][0]):
        x = math.floor(l[i][1] * 0.03)
        total_points += x
    elif "5" in str(l[i][0]):
        x = math.floor(l[i][1] * 0.05)
        total_points += x
    else:
        x = math.floor(l[i][1] * 0.01)
        total_points += x
print(total_points)