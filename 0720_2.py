n = int(input())
l = []
for i in range(n):
    l.append(input().split())
x = 0
for i in range(n):
    if l[i][0] == l[i][1]:
        x += 2
    