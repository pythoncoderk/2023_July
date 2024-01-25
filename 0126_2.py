n, m = map(int, input().split())
l = [int(input()) for i in range(m)]
l2 = [[int(input()) for j in range(m)] for i in range(n)]
# print(l)
# print(l2)
total = []
for i in range(n):
    x = []
    for j in range(m):
        x_c = abs(l[j] - l2[i][j])
        if x_c <= 5:
            x.append(0)
        elif x_c <= 10:
            x.append(1)
        elif x_c <= 20:
            x.append(2)
        elif x_c <= 30:
            x.append(3)
        else:
            x.append(5)
    total.append(100 - sum(x))

max_total = max(total)
if max_total < 0:
    print(0)
else:
    print(max_total)