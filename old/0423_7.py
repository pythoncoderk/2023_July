n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

total_0 = 0
total_1 = 0
total_2 = 0
total_3 = 0
for i in range(n):
    if l[i][0] == 0:
        total_0 += l[i][1]
    elif l[i][0] == 1:
        total_1 += l[i][1]
    elif l[i][0] == 2:
        total_2 += l[i][1]
    elif l[i][0] == 3:
        total_3 += l[i][1]
total = 0
if total_0 != 0:
    total += (total_0 // 100) * 5
if total_1 != 0:
    total += (total_1 // 100) * 3
if total_2 != 0:
    total += (total_2 // 100) * 2
if total_3 != 0:
    total += (total_3 // 100) * 1

print(total)
