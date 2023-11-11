n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
m = input()
l2 = []
for i in range(n):
    if l[i][0] == m:
        l2.append(l[i])
print(l2[0][1])