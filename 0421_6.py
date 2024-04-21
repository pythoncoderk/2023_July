import math
import re

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

points = 0
for i in range(n):
    x = "3" in str(l[i][0])
    y = "5" in str(l[i][0])
    if x == True or y == True:
        x = True
    else:
        x = False
    if x:
        if "3" in str(l[i][0]):
            points += math.floor(l[i][1] * 0.03)
        elif "5" in str(l[i][0]) == "5":
            points += math.floor(l[i][1] * 0.05)
    else:
        points += math.floor(l[i][1] * 0.01)
print(points)
