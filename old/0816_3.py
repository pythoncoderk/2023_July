n = int(input())
l = list(map(int, input().split()))
l2 = [list(map(int, input().split())) for i in range(n)]

total = 0
for i in range(n):
    total_1 = 0
    for j in range(5):
        total_1 += l2[i][j] * l[j]
    if total < total_1:
        total = total_1

print(total)

