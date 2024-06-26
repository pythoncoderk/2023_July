n, m = map(int, input().split())
k1, k2 = map(int, input().split())
l = [int(input()) for i in range(m)]

for i in range(m):
    x = abs(k1 - l[i])
    y = abs(k2 - l[i])
    if x < y:
        print(k1)
    else:
        print(k2)