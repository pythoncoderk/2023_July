n, m = map(int, input().split())
k1, k2 = map(int, input().split())
l = [int(input()) for i in range(m)]

# print(n, m)
# print(k1, k2)
# print(l)

for i in range(m):
    x = abs(l[i] - k1)
    y = abs(l[i] - k2)
    if x >= y:
        print(k2)
    else:
        print(k1)