n, k, m = map(int, input().split())
points = [int(input()) for i in range(n)]
l = []
for i in points:
    if i >= k:
        l.append(i)
if len(l) - m < 0:
    print(0)
else:
    print(len(l) - m)