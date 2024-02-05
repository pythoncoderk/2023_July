n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)
days = []
for i in range(n):
    for j in range(l[i][0], l[i][1]+1):
        days.append(j)
# print(days)

days2 = set(days)
days2 = list(days2)
days2.sort()
# print(days2)

count = 0
for i in range(len(days2)-1):
    if days2[i]+1 == days2[i+1]:
        count += 1
    else:
        count = 0
print(count+1)