x, y = map(int, input().split())
l = [int(input()) for i in range(x)]

if x < y:
    for i in range(y-len(l)):
        l.append(0)

for i in range(y):
    print(l[i])