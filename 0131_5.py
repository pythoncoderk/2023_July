n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(l)

total = []
for i in range(n):
    total.append(l[i][0] + l[i][1])

print(total[0])