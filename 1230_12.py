n, r = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    if min(l[i]) >= r * 2:
        print(i + 1)