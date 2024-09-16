n = int(input())
l = []
for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    l.append([y, x])

l.sort(reverse=True)

for i in range(n):
    print(l[i][1], l[i][0])