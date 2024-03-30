n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, m)
# print(l)

for i in range(n):
    l[i][0] -= l[i][1] * 5
    if l[i][0] < 0:
        l[i][0] = 0
        if l[i][0] >= m:
            print(i+1)
    elif l[i][0] >= m:
        print(i+1)