n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

point = 0
for i in range(n):
    if "3" in str(l[i][0]):
        point += (l[i][1] * 3) // 100
    elif "5" in str(l[i][0]):
        point += (l[i][1] * 5) // 100
    else:
        point += (l[i][1]) // 100

print(point)