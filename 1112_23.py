n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
k = int(input())
l2 = []

answer1 = l[n-1][0]
answer2 = l[n-1][1]

for i in range(len(l)):
    x = abs(l[i][0] - answer1) + abs(l[i][1] - answer2)
    if x <= k:
        l2.append(x)
print(len(l2))
