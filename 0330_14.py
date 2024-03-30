n, m = map(int, input().split())
l = [int(input()) for i in range(m)]

# print(n, m)
# print(l)

points = 0
for i in range(m):
    if l[i] <= points:
        points -= l[i]
    else:
        n -= l[i]
        points += l[i] / 10
    print(n, int(points))